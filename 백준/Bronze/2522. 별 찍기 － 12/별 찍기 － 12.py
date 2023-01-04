N = int(input())

for i in range(1, N):
    print(' '*(N-i), end='')
    print('*'*i)

for j in range(N, 0, -1):
    print(' '*(N-j), end='')
    print('*'*j)