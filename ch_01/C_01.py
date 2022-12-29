from typing import List

# C-1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

# For 2 distinct numbers to have an odd product, they need to be both odd
def find_odd_pair(data: List[int]) -> bool:
    odds = {x for x in data if x % 2}
    return len(odds) >= 2


# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def check_distinct(data: List[int]) -> bool:
    return len(data) == len(set(data))


# C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

print([x**2 - x for x in range(1,11)])


# C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

print([chr(x) for x in range(97,123)])


# C-1.20 Python’s random module includes a function shuﬄe(data) that accepts a
# list of elements and randomly reorders the elements so that each possi-
# ble order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuﬄe function.
from random import randint

def my_shuffle(data: List) -> List:
    n = len(data)
    for i in range(n):
        j = randint(i, n-1)
        data[i], data[j] = data[j], data[i]
    return data
