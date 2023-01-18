# P-1.30 Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

def find_log(n: int) -> int:
    if n < 2:
        return 0
    else:
        return find_log(n / 2) + 1
