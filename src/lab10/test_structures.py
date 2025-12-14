from src.lab10.structures import Stack, Queue


def test_stack():
    print("=== Stack test ===")
    s = Stack()

    assert s.is_empty()
    s.push(1)
    s.push(2)
    s.push(3)

    assert len(s) == 3
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()

    try:
        s.pop()
    except IndexError as e:
        print("OK:", e)

    print("Stack tests passed\n")


def test_queue():
    print("=== Queue test ===")
    q = Queue()

    assert q.is_empty()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    assert len(q) == 3
    assert q.peek() == 10
    assert q.dequeue() == 10
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    assert q.is_empty()

    try:
        q.dequeue()
    except IndexError as e:
        print("OK:", e)

    print("Queue tests passed\n")


if __name__ == "__main__":
    test_stack()
    test_queue()

"""
python3 -m src.lab10.test_structures
"""
