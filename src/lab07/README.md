# Лабораторная работа 7
## test_text

```
import pytest
from lib.text import normalize, tokenize, count_freq, top_n


# normalize
def test_normalize_basic():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"


def test_normalize_empty():
    assert normalize("") == ""


def test_normalize_no_casefold():
    assert normalize("ПрИвЕт", casefold=False) == "ПрИвЕт"


def test_normalize_no_yo2e():
    assert normalize("Ёлка ёж", yo2e=False) == "ёлка ёж"


def test_normalize_multiple_spaces_and_tabs():
    text = "  hello\t\tworld\n\n"
    assert normalize(text) == "hello world"


# tokenize
def test_tokenize_basic():
    assert tokenize("hello world") == ["hello", "world"]


def test_tokenize_hyphenated():
    assert tokenize("text-with-hyphen") == ["text-with-hyphen"]


def test_tokenize_unicode():
    assert tokenize("привет-мир") == ["привет-мир"]


def test_tokenize_numbers_and_words():
    assert tokenize("win10 ubuntu20") == ["win10", "ubuntu20"]


def test_tokenize_apostrophe_split():
    assert tokenize("don't can't i'm") == ["don", "t", "can", "t", "i", "m"]


def test_tokenize_empty():
    assert tokenize("") == []


# count_freq
def test_count_freq_basic():
    tokens = ["a", "b", "a"]
    assert count_freq(tokens) == {"a": 2, "b": 1}


def test_count_freq_case_sensitive():
    tokens = ["a", "A", "a"]
    assert count_freq(tokens) == {"a": 2, "A": 1}


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_count_freq_large_input():
    tokens = ["x"] * 1000
    assert count_freq(tokens) == {"x": 1000}


# top_n
def test_top_n_basic():
    freq = {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]


def test_top_n_tie_breaker():
    freq = {"bbb": 2, "aaa": 2, "ccc": 1}
    # при равной частоте сортировка по алфавиту
    assert top_n(freq, 3) == [("aaa", 2), ("bbb", 2), ("ccc", 1)]


def test_top_n_more_than_available():
    freq = {"x": 10}
    assert top_n(freq, 5) == [("x", 10)]


def test_top_n_empty_dict():
    assert top_n({}, 3) == []
```

## test_json_csv

```
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
```

## Тесты
![Тест ](images/lab07/tests.png)

```
PYTHONPATH=$(pwd)/src pytest -v tests
```