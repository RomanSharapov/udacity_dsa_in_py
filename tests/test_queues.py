from ..queues import Queue


def test_queue():
    # Setup
    q = Queue(1)

    # Test peek on a single-element queue
    assert q.peek() == 1

    # Test dequeue on a single-element queue
    assert q.dequeue() == 1

    # Test enqueue and peek on an empty queue
    q.enqueue(2)
    assert q.peek() == 2

    # Test enqueue and dequeue on a non-empty queue
    q.enqueue(3)
    assert q.dequeue() == 2
    q.enqueue(4)
    assert q.dequeue() == 3
    assert q.dequeue() == 4

    # Test enqueue and peek on an empty queue again
    q.enqueue(5)
    assert q.peek() == 5
