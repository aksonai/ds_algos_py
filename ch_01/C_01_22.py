from typing import List

# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.

def dot_product(a: List[int], b: List[int]) -> List[int]:
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c
