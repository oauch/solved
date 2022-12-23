a, b = input().split()

a = a[::-1]
b = b[::-1]
result = str(int(a) + int(b))

print(int(result[::-1]))