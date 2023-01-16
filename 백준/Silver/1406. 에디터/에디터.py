import sys

N = list(sys.stdin.readline().rstrip())
stack = []

for _ in range(int(sys.stdin.readline())):
    a = list(input().split())
    if a[0] == 'L':
        if N:
            stack.append(N.pop())
    
    elif a[0] == 'D':
        if stack:
            N.append(stack.pop())

    elif a[0] == 'B':
        if N:
            N.pop()
    
    else:
        N.append(a[1])
    
N.extend(reversed(stack))
print(''.join(N))