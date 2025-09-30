# Лабораторная работа 1
## Задание 1

![Первое задание](images/lab01/01_greeting.png)

## Задание 2

![Второе задание](images/lab01/02_sum_avg.png)

## Задание 3

![Третье задание](images/lab01/03_discount_vat.png)

## Задание 4

![Четвёртое задание](images/lab01/04_minutes_to_hhmm.png)

## Задание 5

![Пятое задание](images/lab01/05_initials_and_len.png)

## Задание 6

![Шестое задание](images/lab01/ex06.png)

## Задание 7

![Седьмое задание](images/lab01/ex07.png)


# Лабораторная работа 2
## Задание 1

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


