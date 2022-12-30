import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])

for _ in range(n):
    order = sys.stdin.readline().split()
    one = order[0]

    # push X
    if one == 'push':
        queue.append(order[1])
    
    # pop
    elif one == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    
    # size
    elif one == 'size':
        print(len(queue))

    # empty
    elif one == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    # front
    elif one == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    # back
    elif one == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])