# C-1.26 Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”
from typing import List


def check_arithmetic(a: int, b: int, c: int) -> List[str]:
    results = []
    if a + b == c:
        results.append(f'{a}, {b}, {c} can be used in the operation a + b = c!')
    if a == b - c:
        results.append(f'{a}, {b}, {c} can be used in the operation a = b - c!')
    if a * b == c:
        results.append(f'{a}, {b}, {c} can be used in the operation a * b = c!')
    if not results:
        results.append(f'{a}, {b}, {c} can not be used in any operation!')
    return results


if __name__ == '__main__':
    a = input('Enter number a:\n')
    b = input('Enter number b:\n')
    c = input('Enter number c:\n')
    results = check_arithmetic(int(a), int(b), int(c))
    for r in results:
        print(r)