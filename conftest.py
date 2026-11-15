import re
from pathlib import Path
from uuid import uuid4


import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    """Register options used in pytest.ini and terminal commands."""
    parser.addoption(
        "--browser",
        default="chromium",
        choices=["chromium", "chrome", "msedge", "firefox", "webkit"],
        help="Browser to run tests",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        help="Show the browser window",
    )
    parser.addoption(
        "--base-url",
        default="https://tutorialsninja.com/demo/",
        help="Application URL",
    )
    parser.addoption(
        "--video",
        default="retain-on-failure",
        choices=["on", "off", "retain-on-failure"],
        help="Video recording policy",
    )
    parser.addoption(
        "--screenshot",
        default="only-on-failure",
        choices=["on", "off", "only-on-failure"],
        help="Screenshot capture policy",
    )
    parser.addoption(
        "--tracing",
        default="retain-on-failure",
        choices=["on", "off", "retain-on-failure"],
        help="Playwright tracing policy",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Make test outcomes available during fixture cleanup."""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def browser_context(request):
    """Manage the browser, diagnostic artifacts, and cleanup."""
    config = request.config

    browser_name = config.getoption("browser")
    headed = config.getoption("headed")
    video_mode = config.getoption("video")
    screenshot_mode = config.getoption("screenshot")
    tracing_mode = config.getoption("tracing")

    safe_name = re.sub(r"[^A-Za-z0-9_-]+", "_", request.node.name)[:80]
    artifact_name = f"{safe_name}_{uuid4().hex}"

    reports_dir = Path(config.rootpath) / "reports"
    videos = []
    tracing_started = False

    def track_video(new_page):
        if new_page.video is not None:
            videos.append(new_page.video)

    with sync_playwright() as playwright:
        if browser_name in ("chromium", "chrome", "msedge"):
            channel = {
                "chromium": None,
                "chrome": "chrome",
                "msedge": "msedge",
            }[browser_name]

            browser = playwright.chromium.launch(
                channel=channel,
                headless=not headed,
            )
        elif browser_name == "firefox":
            browser = playwright.firefox.launch(headless=not headed)
        else:
            browser = playwright.webkit.launch(headless=not headed)

        try:
            video_dir = None
            if video_mode != "off":
                video_dir = reports_dir / "videos"
                video_dir.mkdir(parents=True, exist_ok=True)

            context = browser.new_context(record_video_dir=video_dir)
            context.on("page", track_video)

            try:
                if tracing_mode != "off":
                    context.tracing.start(
                        screenshots=True,
                        snapshots=True,
                        sources=True,
                    )
                    tracing_started = True

                yield context

            finally:
                setup_report = getattr(request.node, "rep_setup", None)
                call_report = getattr(request.node, "rep_call", None)

                test_failed = any(
                    report is not None and report.failed
                    for report in (setup_report, call_report)
                )

                keep_screenshot = (
                    screenshot_mode == "on"
                    or (
                        screenshot_mode == "only-on-failure"
                        and test_failed
                    )
                )
                keep_trace = (
                    tracing_mode == "on"
                    or (
                        tracing_mode == "retain-on-failure"
                        and test_failed
                    )
                )
                keep_video = (
                    video_mode == "on"
                    or (
                        video_mode == "retain-on-failure"
                        and test_failed
                    )
                )

                try:
                    try:
                        if keep_screenshot:
                            screenshot_dir = reports_dir / "screenshots"
                            screenshot_dir.mkdir(parents=True, exist_ok=True)

                            for index, open_page in enumerate(context.pages):
                                if open_page.is_closed():
                                    continue

                                screenshot_path = screenshot_dir / (
                                    f"{artifact_name}_{index}.png"
                                )
                                open_page.screenshot(path=screenshot_path)

                              

                    finally:
                        if tracing_started:
                            if keep_trace:
                                trace_dir = reports_dir / "traces"
                                trace_dir.mkdir(parents=True, exist_ok=True)

                                trace_path = trace_dir / (
                                    f"{artifact_name}_trace.zip"
                                )
                                context.tracing.stop(path=trace_path)

                                
                            else:
                                context.tracing.stop()

                finally:
                    # Videos are finalized when the context closes.
                    context.close()

                    for video in videos:
                      if not keep_video:
                       video.delete()
                     
                    

        finally:
            browser.close()


@pytest.fixture
def page(request, browser_context):
    """Open the configured application for each test."""
    test_page = browser_context.new_page()
    test_page.goto(request.config.getoption("base_url"))
    yield test_page