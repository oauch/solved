a = int(input())

if a % 10== 0:
    for i in [300, 60, 10]:
        print(a//i, end=' ')
        a = a % i
else:
    print(-1)