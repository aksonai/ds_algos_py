# P-1.34 A common punishment for school children is to write out a sentence mul-
# tiple times. Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the sentences and it should
# make eight different random-looking typos.

import random

sentence = "I will never spam my friends again."

def make_typos(sentence: str) -> None:
    ascii_letters = list(range(65, 91)) + list(range(97, 123))
    for _ in range(100):
        sentence_list = list(sentence)
        typo_indices = random.sample(range(len(sentence)), 8)
        for i in typo_indices:
            sentence_list[i] = chr(random.choice(ascii_letters))
        print(''.join(sentence_list))


if __name__ == '__main__':
    make_typos(sentence)
