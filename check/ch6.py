import base
from ch5 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "mail0 test OK!",
    "mail1 test OK!",
    "mail2 test OK!",
    "mail3 test OK!",
]

TEMP = [
    "ch6 Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
