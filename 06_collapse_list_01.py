"""
Acquired from: https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1256/#/final-prep

Write a function collapse(lst) that accepts a list of integers as a parameter and returns a new list containing
the result of replacing each pair of integers with the sum of that pair. If the list stores an odd number of elements,
the final element is not collapsed.
"""

import random

def collapse(lst):
    result = []
    # sum pairs
    for i in range(0, len(lst) - 1, 2):
        result.append(lst[i] + lst[i+1])

    # if there's an odd leftover, keep it
    if len(lst) % 2 == 1:
        result.append(lst[-1])

    return result



nums = [random.randint(-100, 100) for _ in range(random.randint(1, 10))]
print(nums)
print(collapse(nums))

