#!/usr/bin/env python3

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""


def get_fib(position):
    """Fibonacci numbers are a sequence of numbers in which
    each number is the sum of the two preceding ones, starting
    from 0 and 1.
    The sequence goes like this:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on."""
    if position < 0:
        raise ValueError("Choose any position that is greater or equal to 0")
    if position in {0, 1}:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)
