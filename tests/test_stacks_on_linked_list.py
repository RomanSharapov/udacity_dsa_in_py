from ..stacks_on_linked_list import Element, LinkedList, Stack


def test_element_creation():
    element = Element(5)
    assert element.value == 5
    assert element.next is None


def test_linkedlist_creation():
    ll = LinkedList()
    assert ll.head is None


def test_linkedlist_append():
    ll = LinkedList()
    element1 = Element(1)
    element2 = Element(2)
    element3 = Element(3)
    ll.append(element1)
    assert ll.head == element1
    ll.append(element2)
    assert ll.head.next == element2
    ll.append(element3)
    assert ll.head.next.next == element3


def test_linkedlist_insert_first():
    ll = LinkedList()
    element1 = Element(1)
    element2 = Element(2)
    element3 = Element(3)
    ll.insert_first(element1)
    assert ll.head == element1
    ll.insert_first(element2)
    assert ll.head == element2
    assert ll.head.next == element1
    ll.insert_first(element3)
    assert ll.head == element3
    assert ll.head.next == element2
    assert ll.head.next.next == element1


def test_linkedlist_delete_first():
    ll = LinkedList()
    element1 = Element(1)
    element2 = Element(2)
    element3 = Element(3)
    ll.append(element1)
    ll.append(element2)
    ll.append(element3)
    node = ll.delete_first()
    assert node == element1
    assert ll.head == element2
    node = ll.delete_first()
    assert node == element2
    assert ll.head == element3
    node = ll.delete_first()
    assert node == element3
    assert ll.head is None


def test_stack_push():
    stack = Stack()
    element1 = Element(1)
    element2 = Element(2)
    element3 = Element(3)
    stack.push(element1)
    assert stack.ll.head == element1
    stack.push(element2)
    assert stack.ll.head == element2
    assert stack.ll.head.next == element1
    stack.push(element3)
    assert stack.ll.head == element3
    assert stack.ll.head.next == element2
    assert stack.ll.head.next.next == element1


def test_stack_pop():
    stack = Stack()
    element1 = Element(1)
    element2 = Element(2)
    element3 = Element(3)
    stack.push(element1)
    stack.push(element2)
    stack.push(element3)
    node = stack.pop()
    assert node == element3
    assert stack.ll.head == element2
    node = stack.pop()
    assert node == element2
    assert stack.ll.head == element1
    node = stack.pop()
    assert node == element1
    assert stack.ll.head is None
