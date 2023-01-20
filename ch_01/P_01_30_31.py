# P-1.30 Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

def find_log(n: int) -> int:
    if n < 2:
        return 0
    else:
        return find_log(n / 2) + 1


# P-1.31 Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.

from typing import Dict
from decimal import Decimal
from collections import OrderedDict


def make_change(charged: Decimal, given: Decimal) -> Dict[str, int]:
    currency_units = OrderedDict({
        'ONE HUNDRED': 10000,
        'TWENTY': 2000,
        'TEN': 1000,
        'FIVE': 500,
        'ONE': 100,
        'HALF': 50,
        'QUARTER': 25,
        'DIME': 10,
        'NICKEL': 5,
        'PENNY': 1,
    })
    change = (given - charged) * 100 # in cents
    change_units = {}
    for k, v in currency_units.items():
        quotient, remainder = divmod(change, v)
        if quotient:
            change_units[k] = int(quotient)
        if not remainder:
            return change_units
        change = remainder
    return change_units
