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
