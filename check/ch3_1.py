import base

EXPECTED = [
    "AAAAAAAAAA [1/5]",
    "BBBBBBBBBB [1/5]",
    "CCCCCCCCCC [1/5]",
    "AAAAAAAAAA [2/5]",
    "BBBBBBBBBB [2/5]",
    "CCCCCCCCCC [2/5]",
    "AAAAAAAAAA [3/5]",
    "BBBBBBBBBB [3/5]",
    "CCCCCCCCCC [3/5]",
    "AAAAAAAAAA [4/5]",
    "BBBBBBBBBB [4/5]",
    "CCCCCCCCCC [4/5]",
    "AAAAAAAAAA [5/5]",
    "BBBBBBBBBB [5/5]",
    "CCCCCCCCCC [5/5]",
    "Test write A OK!",
    "Test write B OK!",
    "Test write C OK!",
]

if __name__ == '__main__':
    base.test_str(EXPECTED)

