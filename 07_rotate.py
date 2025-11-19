"""
Acquired from: https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1256/#/final-prep

Write a function rotate_list_right(numbers, n) that returns a 'rotated' version of a list of integers numbers.
You should rotate numbers to the right n times, so that each element in lst is shifted forward n places,
and the last n elements are moved to the start of the list.
Your function should not change the list that is passed as a parameter, but instead return a new list.
"""


import random

numbers=[]
new_list=[]

size_numbers=random.randint(1,15)
for i in range(size_numbers):
    numbers.append(random.randint(0,100))

n=random.randint(1,5)

def rotate_list_right(numbers,n):
    for i in range(len(numbers)):
        new_list.append(numbers[i-n])
    return new_list

new_list=rotate_list_right(numbers,n)

print(numbers)
print(f"The list above is moved by {n} times to the right.")
print(new_list)

