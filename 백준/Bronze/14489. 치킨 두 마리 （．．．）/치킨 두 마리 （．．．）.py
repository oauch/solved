a, b = map(int, input().split())
c = int(input())

result = 0

if a + b >= c * 2:
    result = a + b - (c * 2)
else:
    result = a + b

print(result)