from pickle import MARK
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


# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.

def count_vowels(s: str) -> int:
    counter = 0
    for ch in s:
        if ch in 'aeiou':
            counter += 1
    return counter


# C-1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For exam-
# ple, if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".


def remove_punctuation(s: str) -> str:
    MARKS = ['.', ',', '?', '!', ';', ':', '(', ')', '[', ']', '{', '}', '"', '\'',
         '...', '-', '~']
    new_str = ''
    for ch in s:
        if ch not in MARKS:
            new_str += ch
    return new_str
