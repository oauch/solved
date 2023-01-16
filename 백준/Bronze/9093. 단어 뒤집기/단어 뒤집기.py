T = int(input())

for _ in range(T):
    txt = input().split()
    for i in txt:
        print(i[::-1], end=' ')