import base

EXPECTED = [
    """Hello world from user mode program!
Test hello_world OK!""",
    """Test power OK!""",
    """string from data section
strinstring from stack section
strin
Test write1 OK!""",
]

TEMP = [
    """Test write0 OK!""",
    """Test hello_world OK!""",
    """Test write1 OK!""",
]

NOT_EXPECTED = [
    "FAIL: T.T",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
