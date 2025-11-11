"""
Acquired from: https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1256/#/final-prep

Interesting List
Write a function make_interesting(num_list) that accepts a list of integers and returns a new list based on the given
list. The new list should have each of the values in num_list as follows:
if the integer in num_list is less than zero, the new list should not have this value;
if the integer in num_list is greater than or equal to zero and odd, the new list should have this integer value with
10 added to it;
if the integer in num_list is greater than or equal to zero and even, the new list should have this integer value
unchanged.

We'll consider the number 0 to be even.

Here are some sample calls to make_interesting and what should be returned.

make_interesting([-2, 33, 14, 6, -13, 9, 2])   [43, 14, 6, 19, 2]
make_interesting([1, 2, 3, 4, 5])    [11, 2, 13, 4, 15]
make_interesting([-10, -20, -5]) []"""

import random

num_list=[]

for i in range(7):
    num_list.append(random.randint(-100,100))
print(num_list)

def make_interesting(num_list):
    for i in range(len(num_list)-1,-1,-1): # If (A,0,-1) used, then zeroth index is skipped. Pop eliminates the last value so you have to start from the last value and count backwards.
        if num_list[i] < 0:
            num_list.pop(i) # If remove is used, problem of eliminating values who are repeated in the serries.
        elif num_list[i] >=0 and num_list[i]%2 != 0:
            num_list[i]=num_list[i]+10

make_interesting(num_list)
print(num_list)

