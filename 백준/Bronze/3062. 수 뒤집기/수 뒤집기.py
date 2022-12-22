t = int(input())

for _ in range(t):
    n = input()
    rev = str(int(n) + int(n[::-1]))
    if rev == rev[::-1]:
        print("YES")
    else:
        print("NO")