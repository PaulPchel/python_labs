from pathlib import Path
import json
import csv
from openpyxl import Workbook, load_workbook

base = Path(__file__).resolve().parents[2]
samples = base / "data" / "samples"
out = base / "data" / "out"

# №1
print("Пример 1: CSV -> XLSX")
csv_path = samples / "people.csv"
xlsx_path = out / "people.xlsx"

if csv_path.exists():
    with csv_path.open(encoding="utf-8") as f:
        csv_rows = list(csv.reader(f))

    if not csv_rows:
        print(f"CSV файл пустой: {csv_path.name}")
    else:
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"
        for row in csv_rows:
            ws.append(row)

        for column_cells in ws.columns:
            length = max(len(str(cell.value)) for cell in column_cells)
            ws.column_dimensions[column_cells[0].column_letter].width = max(length, 8)

        wb.save(xlsx_path)
        print(f"Использован CSV: {csv_path.name}")
        print(f"XLSX строки: {len(csv_rows)}")
else:
    print(f"CSV файл не найден: {csv_path.name}")


# №2
print("Пример 2: JSON -> CSV")
json_path = samples / "people.json"
csv_out_path = out / "people_from_json.csv"

if json_path.exists():
    with json_path.open(encoding="utf-8") as f:
        data_json = json.load(f)

    if not data_json:
        print(f"JSON файл пустой: {json_path.name}")
    else:
        fieldnames = list(data_json[0].keys())
        with csv_out_path.open("w", newline="", encoding="utf-8") as f_out:
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_json)
        print(f"Использован JSON: {json_path.name}")
        print(f"CSV строки: {len(data_json)}")
else:
    print(f"JSON файл не найден: {json_path.name}")


# №3
print("Пример 3: CSV → JSON")
csv_path = samples / "people.csv"
json_out_path = out / "people_from_csv.json"

if csv_path.exists():
    with csv_path.open(encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    if not reader:
        print(f"CSV файл пустой: {csv_path.name}")
    else:
        with json_out_path.open("w", encoding="utf-8") as f_out:
            json.dump(reader, f_out, ensure_ascii=False, indent=2)

        print(f"Использован CSV: {csv_path.name}")
        print(f"JSON записи: {len(reader)}")
else:
    print(f"CSV файл не найден: {csv_path.name}")


"""
Для запуска по очереди вставляешь в терминал:
cd ~/Desktop/python_labs
export PYTHONPATH=$PWD/src
python3 -m lab05.test
"""

