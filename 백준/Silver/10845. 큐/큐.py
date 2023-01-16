import sys

N = int(sys.stdin.readline())
result = []

for _ in range(N):
    a = sys.stdin.readline().split()
    
    # push
    if a[0] == 'push':
        result.append(a[1])

    # pop
    elif a[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop(0))

    # size
    elif a[0] == 'size':
        print(len(result))
    
    # empty
    elif a[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)

    # front
    elif a[0] == 'front':
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])

    # back
    elif a[0] == 'back':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])