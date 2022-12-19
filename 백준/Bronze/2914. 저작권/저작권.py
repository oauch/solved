a, i = map(int, input().split())

if a * i == i:
    print(a * i)
elif a * i == a:
    print(a * i)
else:
    print((a * (i-1))+1)