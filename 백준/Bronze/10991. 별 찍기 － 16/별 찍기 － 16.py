N = int(input())

for i in range(1, N+1):
    print(' '*(N-i), end='')
    if N == 1:
        print('*'*i)
    else:
        print('* '*i)