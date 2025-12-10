from src.lab09.group import Group, Student

def main():
    storage = "data/lab09/students.csv"
    group = Group(storage)
    
    group.pretty_print(group.list())

"""
Еще тесты других функций:


    group.pretty_print(group.list())

    
    group.add(Student("Козлов Козьма", "2005-05-05", "SE-02", 4.7))
    print("После добавления:")
    group.pretty_print()

    
    print("Поиск 'Иван':")
    group.pretty_print(group.find("Иван"))


    group.update("Иванов Иван", gpa=4.5)
    print("После обновления GPA Иванова Ивана:")
    group.pretty_print()


    group.remove("Сидоров Сидор")
    print("После удаления Сидорова Сидора:")
    group.pretty_print()
"""

if __name__ == "__main__":
    main()


"""
python3 -m src.lab09.test
"""
