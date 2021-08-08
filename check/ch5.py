import base
from ch4 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    r"Test getpid OK51135! pid = (\d+)",
    "Test spawn0 OK51135!",
    "Test wait OK51135!",
    "Test waitpid OK51135!",
]

TEMP = [
    "ch5 Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
