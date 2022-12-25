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
