a = []
result = 0

for _ in range(5):
    a.append(input())

for i in a:
    result += int(i)
print(result)