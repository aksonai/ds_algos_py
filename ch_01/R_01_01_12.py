from typing import List, Tuple


# R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiple(n: int, m: int) -> bool:
    return not n % m


# R-1.2 Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(k: int) -> bool:
    return bin(k)[-1] == '0'


# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data: List[int]) -> Tuple[int, int]:
    min_val = data[0]
    max_val = data[0]
    for x in data:
        if x < min_val:
            min_val = x
        elif x > max_val:
            max_val = x

    return (min_val, max_val)


# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_squares(n: int) -> int:
    s = 0
    for x in range(n):
        s += x**2
    return s


# R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying 
# on Python’s comprehension syntax and the built-in sum function.

def sum_squares2(n: int) -> int:
    return sum([x**2 for x in range(n)])


# R-1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sum_square_odd(n: int) -> int:
    s = 0
    for x in range(n):
        if x % 2:
            s += x**2
    return s


# R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
# ing on Python’s comprehension syntax and the built-in sum function.

def sum_square_odd2(n: int) -> int:
    return sum([x**2 for x in range(n) if x % 2])


# R-1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for in-
# dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?

s = 'abcdefghijkl'
k=-3
n=len(s)
# print(s[k])
# print(s[k+n])


# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

# print(list(range(50, 81, 10)))


# R-1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

# print(list(range(8, -9, -2)))


# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

# print([2**x for x in range(9)])


# R-1.12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module in-
# cludes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.
from random import randrange

def my_choice(data):
    index = randrange(len(data))
    return data[index]
