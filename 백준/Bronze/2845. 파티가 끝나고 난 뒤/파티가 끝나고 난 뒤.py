L, P = map(int, input().split())
result = L * P
a = list(map(int, input().split()))

for i in a:
    print(i - result, end=' ')