import sys

n = int(sys.stdin.readline())
result = 0

for i in range(n):
    a = int(sys.stdin.readline())
    result += a
    result -= 1
print(result+1)