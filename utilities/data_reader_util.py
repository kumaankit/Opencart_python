import json
import csv
import openpyxl


def read_json_data(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        records = json.load(file)

    data = [tuple(record.values()) for record in records]

    if not data:
        raise ValueError(f"No test data found in '{file_path}'")

    return data


def read_csv_data(file_path: str):
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = [tuple(row.values()) for row in reader]

    if not data:
        raise ValueError(f"No test data found in '{file_path}'")

    return data

def read_excel_data(file_path: str, sheet_name: str = None):
    """Read Excel test data; fail if reading fails or no data exists."""
    workbook = openpyxl.load_workbook(file_path)

    try:
        sheet = workbook[sheet_name] if sheet_name else workbook.active

        data = [
            row
            for row in sheet.iter_rows(min_row=2, values_only=True)
            if any(value is not None for value in row)
        ]

        if not data:
            raise ValueError(
                f"No test data found in '{file_path}', "
                f"sheet '{sheet.title}'"
            )

        return data
    finally:
        workbook.close()