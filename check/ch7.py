import base
from ch6 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "Test file0 OK51135!",
    "Test fstat OK51135!",
    "Test link OK51135!",
]

TEMP = [
    "ch7 Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
