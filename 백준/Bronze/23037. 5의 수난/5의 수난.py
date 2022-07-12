import sys

n = sys.stdin.readline()[:-1]
result = 0
for c in n:
    result += int(c) ** 5
print(result)