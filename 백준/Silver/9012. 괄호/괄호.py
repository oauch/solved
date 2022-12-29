import sys

T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    order = sys.stdin.readline()

    for i in order:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
        else:
            if not stack:
                print("YES")
            else:
                print("NO")