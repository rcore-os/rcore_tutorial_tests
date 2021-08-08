import base
from ch5 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "mail0 test OK51135!",
    "mail1 test OK51135!",
    "mail2 test OK51135!",
    "mail3 test OK51135!",
]

TEMP = [
    "ch6 Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
