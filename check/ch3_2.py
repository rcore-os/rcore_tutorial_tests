import sys
import re

PATTERN = r"priority = (\d+), exitcode = (\d+)"

output = sys.stdin.read(1000000)

result = re.compile(PATTERN).findall(output)
assert len(result) == 6


def factor(match):
    priority, exitcode = match
    priority = int(priority)
    exitcode = int(exitcode)
    return exitcode // priority


factors = list(map(factor, result))
print('exitcode / priority =', factors)

if max(factors) / min(factors) < 1.5:
    print('\n\033[92m[PASS]\033[0m Stride Test')
    print('\nTest passed: 1/1')
else:
    print('\n\033[91m[FAIL]\033[0m Stride Test')
    print('\nTest passed: 0/1')
    assert False
