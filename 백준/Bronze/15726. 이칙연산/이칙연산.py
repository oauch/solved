# print(32*16//8) 출력 : 64

a, b, c = map(int, input().split())


if b > c:
    print(a * b // c)
elif c > b:
    print(a * c // b)