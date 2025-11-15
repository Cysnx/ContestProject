"""
Acquired from: https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1256/#/final-prep

Write a function collapse(lst) that accepts a list of integers as a parameter and returns a new list containing
the result of replacing each pair of integers with the sum of that pair. If the list stores an odd number of elements,
the final element is not collapsed.
"""

import random

num_list=[]
new_list=[]

for i in range(random.randint(1,10)):
    num_list.append(random.randint(-100,100))
print(num_list)

def collapse_list(num_list):
    if len(num_list) % 2 == 0:
        for i in range(1,len(num_list),2):
            new_list.append(num_list[i]+num_list[i-1])
    else:
        for i in range(1,len(num_list),2):
            new_list.append(num_list[i]+num_list[i-1])
        new_list.append(num_list[-1])
    print(new_list)

collapse_list(num_list)

