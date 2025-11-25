import json
import csv
import pytest
from pathlib import Path
from lab05.json_csv import json_to_csv, csv_to_json


# json_to_csv
def test_json_to_csv_basic(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())
    assert rows[0]["name"] == "Alice"


def test_json_to_csv_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        json_to_csv(str(tmp_path / "missing.json"), str(tmp_path / "out.csv"))


def test_json_to_csv_invalid_extension(tmp_path):
    bad = tmp_path / "file.txt"
    bad.write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(bad), str(tmp_path / "out.csv"))


def test_json_to_csv_empty_json(tmp_path):
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


# csv_to_json
def test_csv_to_json_basic(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "20"})
        writer.writerow({"name": "Bob", "age": "30"})

    csv_to_json(str(src), str(dst))

    content = json.loads(dst.read_text(encoding="utf-8"))
    assert len(content) == 2
    assert {"name", "age"} <= set(content[0].keys())
    assert content[0]["name"] == "Alice"


def test_csv_to_json_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        csv_to_json(str(tmp_path / "missing.csv"), str(tmp_path / "out.json"))


def test_csv_to_json_invalid_extension(tmp_path):
    bad = tmp_path / "file.txt"
    bad.write_text("a,b\n1,2", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(bad), str(tmp_path / "out.json"))


def test_csv_to_json_empty_csv(tmp_path):
    src = tmp_path / "empty.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))
