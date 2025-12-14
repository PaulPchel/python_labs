from src.lab10.linked_list import SinglyLinkedList


def test_linked_list():
    print("=== SinglyLinkedList test ===")
    lst = SinglyLinkedList()

    assert len(lst) == 0

    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert list(lst) == [1, 2, 3]

    lst.prepend(0)
    assert list(lst) == [0, 1, 2, 3]

    lst.insert(2, 99)
    assert list(lst) == [0, 1, 99, 2, 3]

    lst.remove_at(2)
    assert list(lst) == [0, 1, 2, 3]

    lst.remove_at(0)
    assert list(lst) == [1, 2, 3]

    lst.remove_at(len(lst) - 1)
    assert list(lst) == [1, 2]

    try:
        lst.remove_at(10)
    except IndexError as e:
        print("OK:", e)

    print("List content:", lst)
    print("Pretty view:", lst.pretty())
    print("LinkedList tests passed\n")


if __name__ == "__main__":
    test_linked_list()

"""
python3 -m src.lab10.test_linked_list
"""
