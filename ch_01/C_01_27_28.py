# C-1.27 In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementa-
# tions, from page 41, was the most efﬁcient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance ad-
# vantages.

def factors(n):
    k=1
    larger_factors = []
    while k * k < n:
        if n % k == 0:
            yield k
            larger_factors.append(n // k)
        k += 1
    if k * k == n:
        yield k
    while larger_factors:
        yield larger_factors.pop()


# C-1.28 For the special case of p = 2, this results in the traditional Euclidean
# norm, which represents the length of the vector. For example, the Euclidean 
# norm of a two-dimensional vector with coordinates (4, 3) has a Euclidean norm 
# of 5. Give an implementation of a function named norm such that norm(v, p) 
# returns the p-norm value of v and norm(v) returns the Euclidean norm of v. 
# You may assume that v is a list of numbers.
from typing import List


def norm(v: List[int], p: int) -> int:
    return int(sum([x ** p for x in v]) ** (1/p))
