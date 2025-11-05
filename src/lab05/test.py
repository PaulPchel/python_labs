from pathlib import Path
import json, csv
from lab05.csv_xlsx import csv_to_xlsx
from lab05.json_csv import json_to_csv, csv_to_json

base = Path(__file__).resolve().parents[2]
samples = base / "data" / "samples"
out = base / "data" / "out"

# №1
print("Пример 1: CSV → XLSX")
src_csv = samples / "people.csv"
dst_xlsx = out / "people.xlsx"
try:
    csv_to_xlsx(src_csv, dst_xlsx)
    print(f"Использован CSV: {src_csv.name}")
    print("Файл XLSX успешно перезаписан")
except Exception as e:
    print(f"Ошибка: {e}")


# №2
print("Пример 2: JSON → CSV")
src_json = samples / "people.json"
dst_csv = out / "people_from_json.csv"
try:
    json_to_csv(src_json, dst_csv)
    with dst_csv.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"Использован JSON: {src_json.name}")
    print(f"CSV строки: {len(rows)}")
except Exception as e:
    print(f"Ошибка: {e}")


# №3
print("Пример 3: CSV → JSON")
src_csv2 = samples / "people.csv"
dst_json = out / "people_from_csv.json"
try:
    csv_to_json(src_csv2, dst_json)
    with dst_json.open(encoding="utf-8") as f:
        data_json = json.load(f)
    print(f"Использован CSV: {src_csv2.name}")
    print(f"JSON записи: {len(data_json)}")
except Exception as e:
    print(f"Ошибка: {e}")


"""
Для запуска по очереди вставляешь в терминал:
cd ~/Desktop/python_labs
export PYTHONPATH=$PWD/src
python3 -m lab05.test
"""

