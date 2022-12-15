a = int(input())
for i in range(a, -1, -1):
    if a > i:
        print(' '* abs(i-a), end='')
    print('*' * i)