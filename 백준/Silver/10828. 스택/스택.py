import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    order = sys.stdin.readline().split()
    A = order[0]

    # push
    if A == 'push':
        B = order[1]
        stack.append(B)
    
    # pop
    elif A == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    # size
    elif A == 'size':
        print(len(stack))

    # empty
    elif A == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # top
    elif A == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])