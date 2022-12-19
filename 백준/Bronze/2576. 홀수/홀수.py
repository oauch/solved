import sys
input = sys.stdin.readline

a_result = []

for i in range(7):
    a = int(input())
    if a % 2 == 1:
        a_result.append(a)
if a_result:
    print(sum(a_result))
    print(min(a_result))
else:
    print(-1)