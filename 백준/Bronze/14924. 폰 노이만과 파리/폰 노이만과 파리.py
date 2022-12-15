a, b, c = map(int, input().split())

hour = c // (a*2)
result = hour * b
print(result)