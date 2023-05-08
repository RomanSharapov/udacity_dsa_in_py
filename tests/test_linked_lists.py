#!/usr/bin/env python3

from ..linked_lists import Element, LinkedList


def test_append():
    # Test appending to an empty list
    linked_list = LinkedList()
    new_element = Element(1)
    linked_list.append(new_element)
    assert linked_list.head == new_element

    # Test appending to a non-empty list
    new_element_2 = Element(2)
    linked_list.append(new_element_2)
    assert linked_list.head.next == new_element_2


def test_get_position():
    # Test getting an element from the beginning of the list
    linked_list = LinkedList()
    element_1 = Element(1)
    element_2 = Element(2)
    linked_list.append(element_1)
    linked_list.append(element_2)
    assert linked_list.get_position(1) == element_1

    # Test getting an element from the middle of the list
    assert linked_list.get_position(2) == element_2

    # Test getting an element from the end of the list
    assert linked_list.get_position(3) == None


def test_insert():
    # Test inserting a new element at the beginning of the list
    linked_list = LinkedList()
    element_1 = Element(1)
    element_2 = Element(2)
    linked_list.insert(element_1, 1)
    linked_list.insert(element_2, 1)
    assert linked_list.head == element_2

    # Test inserting a new element in the middle of the list
    element_3 = Element(3)
    linked_list.insert(element_3, 2)
    assert linked_list.get_position(2) == element_3

    # Test inserting a new element at the end of the list
    element_4 = Element(4)
    linked_list.insert(element_4, 4)
    assert linked_list.get_position(4) == element_4


def test_delete():
    # Test deleting the first node with a given value
    linked_list = LinkedList()
    element_1 = Element(1)
    element_2 = Element(2)
    linked_list.append(element_1)
    linked_list.append(element_2)
    linked_list.delete(1)
    assert linked_list.head == element_2

    # Test deleting a node that doesn't exist in the list
    linked_list.delete(3)
    assert linked_list.head == element_2
