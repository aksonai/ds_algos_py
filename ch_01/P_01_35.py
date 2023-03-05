# P-1.35 The birthday paradox says that the probability that two people in a room
# will have the same birthday is more than half, provided n, the number of
# people in the room, is more than 23. This property is not really a paradox,
# but many people ﬁnd it surprising. Design a Python program that can test
# this paradox by a series of experiments on randomly generated birthdays,
# which test this paradox for n = 5, 10, 15, 20, . . . , 100.

from datetime import date
from random import randint


def random_bday() -> date:
    ordinal_start_date = date(2023, 1, 1).toordinal()
    random_day = randint(0, 364)
    return date.fromordinal(ordinal_start_date + random_day)


def test_for_sample(size: int) -> bool:
    bdays = []
    for _ in range(size):
        bday = random_bday()
        if bday in bdays:
            return True
        bdays.append(bday)
    return False

if __name__ == '__main__':
    for size in range(5, 105, 5):
        result = test_for_sample(size)
        print(f'For {size} it is {result}!')
