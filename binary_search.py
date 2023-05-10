#!/usr/bin/env python3

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Binary search implementation.
    This function takes a sorted array and an item. If the
    item in the array, the function returns its position.
    Otherwise, it returns -1."""
    low, high = 0, len(input_array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = input_array[mid]
        if value == guess:
            return mid
        if value > guess:
            low = mid + 1
        if value < guess:
            high = mid - 1
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
