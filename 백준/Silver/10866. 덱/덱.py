import sys
from collections import deque

N = int(sys.stdin.readline())
deque = deque()

for _ in range(N):
    answer = sys.stdin.readline().split()

    if answer[0] == 'push_front':
        deque.appendleft(answer[1])
    
    elif answer[0] == 'push_back':
        deque.append(answer[1])
    
    elif answer[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())

    elif answer[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())

    elif answer[0] == 'size':
        print(len(deque))

    elif answer[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    
    elif answer[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif answer[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])