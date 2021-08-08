import base
from ch2 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "Test set_priority OK!",
    r"get_time OK! (\d+)",
    "Test sleep OK!",
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
