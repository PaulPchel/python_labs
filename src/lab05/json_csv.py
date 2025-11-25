import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")
    if not json_file.suffix.lower() == ".json":
        raise ValueError("Неверный тип файла, ожидается .json")

    with json_file.open(encoding="utf-8") as f:
        data = json.load(f)

    if (
        not data
        or not isinstance(data, list)
        or not all(isinstance(x, dict) for x in data)
    ):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    fieldnames = list(data[0].keys())

    with csv_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
    if not csv_file.suffix.lower() == ".csv":
        raise ValueError("Неверный тип файла, ожидается .csv")

    with csv_file.open(encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    if not reader:
        raise ValueError("Пустой CSV или отсутствует заголовок")

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(reader, f, ensure_ascii=False, indent=2)
