import sys

n = int(sys.stdin.readline())
count = 0
stack = []
result = []
no = True

for _ in range(n):
    order = int(sys.stdin.readline())

    while count < order:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == order:
        stack.pop()
        result.append('-')
    else:
        no = False
        break

if no == False:
    print("NO")
else:
    for i in result:
        print(i)