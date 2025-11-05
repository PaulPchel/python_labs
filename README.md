# Лабораторная работа 1
## Задание 1

![Первое задание](images/lab01/01_greeting.png)

```
name=str(input('Имя: '))
age=int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

## Задание 2

![Второе задание](images/lab01/02_sum_avg.png)

```
a=float(input('a: ').replace(',','.'))
b=float(input('b: ').replace(',','.'))
sum=round(a+b,2)
avg=round(sum/2,2)
print(f'sum={sum}; avg={avg}')
```

## Задание 3

![Третье задание](images/lab01/03_discount_vat.png)

```
price=float(input('Цена: '))
discount=float(input('Скидка: '))
vat=float(input('НДС: '))

base=round(price*(1 - discount/100),2)
vat_amount=round(base*(vat/100),2)
total=round(base+vat_amount,2)

print(f'База после скидки: {base} ₽')
print(f'НДС:               {vat_amount} ₽')
print(f'Итого к оплате:    {total} ₽')
```

## Задание 4

![Четвёртое задание](images/lab01/04_minutes_to_hhmm.png)

```
m=int(input("Минуты: "))
hours=m//60
minutes=m%60
print(f'{hours}:{minutes:02d}')
```

## Задание 5

![Пятое задание](images/lab01/05_initials_and_len.png)

```
name=input("ФИО: ")

parts=name.strip().split()
final=" ".join(parts)

initials=''.join(i[0].upper() for i in parts)
length=len(final)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {length}")
```

## Задание 6

![Шестое задание](images/lab01/ex06.png)

```
n = int(input('Количество: '))
ochno = 0
zaochno = 0

for i in range(n):
    line=input('Участник: ').split()
    format_uch=line[-1]

    if format_uch=="True":
        ochno+=1
    else:  
        zaochno+=1

print(ochno, zaochno)
```

## Задание 7

![Седьмое задание](images/lab01/ex07.png)

```
s = input().strip()

start=0
for i, ch in enumerate(s):
    if ch.isupper():
        start=i
        break

second=0
for i, ch in enumerate(s):
    if ch.isdigit() and i+1<len(s):
        second=i+1
        break

step=second- start

result=''
i=start
while i<len(s):
    if s[i]=='.':
        result+='.'
        break
    result+=s[i]
    i+=step

print(result)
```


# Лабораторная работа 2
## Задание 1

### arrays(min_max)
![Первое задание; Первая функция](images/lab02/arrays(min_max).png)

```
from typing import List, Tuple

def min_max(nums: List[float|int]) -> Tuple[float|int, float|int]:
    if not nums:
        return 'ValueError'   

    min_val = max_val = nums[0]
    for x in nums[1:]:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    return min_val, max_val
```

### arrays(unique_sorted)
![Первое задание; Вторая функция](images/lab02/arrays(unique_sorted).png)

```
from typing import List

def unique_sorted(nums: List[float | int]) -> List[float | int]:
    unique: List[float | int] = []
    
    for x in nums:
        if x not in unique:
            unique.append(x)
    
    unique.sort()
    
    return unique
```

### arrays(flatten)
![Первое задание; Третья функция](images/lab02/arrays(flatten).png)

```
from typing import List

def flatten(mat: List[list | tuple]) -> List:
    result: List = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            return ('TypeError')
        for elem in row:
            result.append(elem)
    return result
```

## Задание B

### matrix(transpose)
![Задание B; Первая функция](images/lab02/matrix(transpose).png)

```
from typing import List

def transpose(mat: List[List[float|int]]) -> List[List]:
    if not mat:
        return []

    row_len = len(mat[0])
    if any(len(row) != row_len for row in mat):
        return 'ValueError'
    
    return [list(col) for col in zip(*mat)]
```

### matrix(row_sums)
![Задание B; Вторая функция](images/lab02/matrix(row_sums).png)

```
from typing import List

def row_sums(mat: List[List[float|int]]) -> List[float]:
    if not mat:
        return []
    
    row_len = len(mat[0])
    if any(len(row) != row_len for row in mat):
        return 'ValueError'
    
    return [sum(row) for row in mat]
```

### matrix(col_sums)
![Задание B; Третья функция](images/lab02/matrix(col_sums).png)

```
from typing import List

def col_sums(mat:List[List[float|int]]) -> List[float]:
    if not mat:
        return []
    
    row_len = len(mat[0])
    if any(len(row) != row_len for row in mat):
        return 'ValueError'
    
    return [sum(row[i] for row in mat) for i in range(row_len)]
```

## Задание C

![Задание C](images/lab02/tuples.png)

```
def format_record(rec: tuple[str, str, float]) -> str:

    fio, group, gpa = rec
    if not (isinstance(fio, str) and isinstance(group, str)) or not isinstance(gpa, (int, float)):
        return 'Неверные типы данных'
    
    parts = " ".join(fio.strip().split()).split()
    if len(parts) < 2 or not group.strip():
        return 'Некорректное ФИО или группа'
    
    surname = parts[0].capitalize()
    initials = "".join(p[0].upper() + "." for p in parts[1:3])
    
    return f'{surname} {initials}, гр. {group.strip()}, GPA {gpa:.2f}'
```


# Лабораторная работа 3
## Задание A

### normalize
![Первое задание; Первая функция](images/lab03/text(normalize).png)

```
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = re.sub(r'[\r\n\t\f\v]', ' ', text)

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    if casefold:
        text = text.casefold()

    text = re.sub(r'\s+', ' ', text).strip()

    return text

print(normalize('ПрИвЕт\nМИр\t'))
print(normalize('ёжик, Ёлка'))
print(normalize('Hello\r\nWorld'))
print(normalize('  двойные   пробелы  '))
```

### tokenize
![Первое задание; Вторая функция](images/lab03/text(tokenize).png)

```
import re

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text, flags=re.UNICODE)

print(tokenize('привет мир'))
print(tokenize('hello,world!!!'))
print(tokenize('по-настоящему круто'))
print(tokenize('2025 год'))
print(tokenize('emoji 😀 не слово'))
```

### count_freq
![Первое задание; Третья функция](images/lab03/text(count_freq).png)

```
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return dict(sorted_items)

print(count_freq(['a', 'b', 'a', 'c', 'b', 'a']))
print(count_freq(['bb', 'aa', 'bb', 'aa', 'cc']))
```

### top_n
![Первое задание; Четвёртая функция](images/lab03/text(top_n).png)

```
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

freq1 = {'a': 3, 'b': 2, 'c': 1}
print(top_n(freq1, n=2))

freq2 = {'bb': 2, 'aa': 2, 'cc': 1}
print(top_n(freq2, n=2))
```

## Задание B

### text_stats
![Задание B](images/lab03/text_stats.png)

```
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n

def main() -> None:
    text = sys.stdin.read().strip()

    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()

"""
1. Сначала вставляешь в терминал  python3 src/lab03/text_stats.py
2. Затем втсавляешь текст, то есть Привет, мир! Привет!!!
3. Потом клавишами CTRL+D
"""
```


# Лабораторная работа 4
## Задание A

### io_txt_csv

```
from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Прочитать текстовый файл и вернуть его содержимое как одну строку.

    Исключения:
        FileNotFoundError: если файл не найден.
        UnicodeDecodeError: если содержимое не может быть декодировано указанной кодировкой.
    """
    path = Path(path)
    with path.open("r", encoding=encoding) as f:
        return f.read()


def write_csv(
    rows: list[tuple | list],
    path: str | Path,
    header: tuple[str, ...] | None = None
) -> None:
    """
    Создать или перезаписать CSV-файл с разделителем запятая (,).

    Исключения:
        ValueError: если строки в `rows` имеют разную длину.
    """
    if not rows:
        with Path(path).open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if header:
                writer.writerow(header)
        return

    expected_len = len(rows[0])
    if any(len(row) != expected_len for row in rows):
        raise ValueError("Все строки должны иметь одинаковую длину")

    path = Path(path)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)
```

## Задание B

### text_report
![Задание B](images/lab04/text_report.png)

```
import sys
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Генерация отчёта по частоте слов в тексте.")
    parser.add_argument(
        "--in", dest="input_path", default="data/lab04/input.txt",
        help="путь к входному файлу (по умолчанию: data/lab04/input.txt)"
    )
    parser.add_argument(
        "--out", dest="output_path", default="data/lab04/report.csv",
        help="путь к выходному CSV (по умолчанию: data/lab04/report.csv)"
    )
    args = parser.parse_args()

    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    text = read_text(input_path)
    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    rows = [(word, count) for word, count in sorted_items]

    write_csv(rows, output_path, header=("word", "count"))

    total_words = len(tokens)
    unique_words = len(freq)
    top5 = top_n(freq, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()

"""
Для запуска:
python3 src/lab04/text_report.py --in /Users/paulpchelintsev/Desktop/python_labs/data/lab04/input.txt
"""
```


# Лабораторная работа 5
## Задание A

### iJSON ↔ CSV (json_csv)

```
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

    if not data or not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    fieldnames = list(data[0].keys())

    # Только создаём файл, если его ещё нет
    if not csv_file.exists():
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

    if not json_file.exists():
        with json_file.open("w", encoding="utf-8") as f:
            json.dump(reader, f, ensure_ascii=False, indent=2)
```

## Задание B

### CSV → XLSX (csv_xlsx)

```
import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)

    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
    if not csv_file.suffix.lower() == ".csv":
        raise ValueError("Неверный тип файла, ожидается .csv")

    # Создаём XLSX только если его нет
    if not xlsx_file.exists():
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        with csv_file.open(encoding="utf-8") as f:
            for row in csv.reader(f):
                ws.append(row)

        # автоширина колонок
        for column_cells in ws.columns:
            length = max(len(str(cell.value)) for cell in column_cells)
            ws.column_dimensions[column_cells[0].column_letter].width = max(length, 8)

        wb.save(xlsx_file)
```

## Тесты

### test
![Тест](images/lab05/test.png)

```
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
```

