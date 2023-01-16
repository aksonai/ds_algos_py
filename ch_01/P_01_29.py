# P-1.29 Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.
from typing import List


all_combinations = []

def get_combinations(letters: List[str], combination: List[str]) -> None:
    global all_combinations
    if len(letters) == 0:
        all_combinations.append(''.join(combination))
    else:
        for i in range(len(letters)):
            combination.append(letters.pop(i))
            get_combinations(letters, combination)
            letters.insert(i, combination.pop())

if __name__ == '__main__':
    get_combinations(list('catdog'), [])
    print(all_combinations)
