import base

EXPECTED = [
    """Hello world from user mode program!
Test hello_world OK51135!""",
    """Test power OK51135!""",
    """string from data section
strinstring from stack section
strin
Test write1 OK51135!""",
]

TEMP = [
    """Test write0 OK51135!""",
    """Test hello_world OK51135!""",
    """Test write1 OK51135!""",
]

NOT_EXPECTED = [
    "FAIL: T.T",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
