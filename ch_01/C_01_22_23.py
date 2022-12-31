from typing import List

# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.

def dot_product(a: List[int], b: List[int]) -> List[int]:
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c


# C-1.23 Give an example of a Python code fragment that attempts to write an ele-
# ment to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”

def write_to_list(A: List, index: int, value) -> List:
    try:
        A[index] = value
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")
    return A
