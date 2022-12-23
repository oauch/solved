t = int(input())

for _ in range(t):
    c, n = map(int, input().split())
    if c % n == 0:
        print(c // n)
    else:
        print((c // n) + 1)