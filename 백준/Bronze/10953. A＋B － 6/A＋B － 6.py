t = int(input())

for _ in range(t):
    a = input().split(',')
    result = 0
    for i in a:
        result += int(i)
    print(result)