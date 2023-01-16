import sys

n = int(sys.stdin.readline())
count = 0       # 스택 카운트
stack = []      # 스택 리스트
result = []     # 결과 리스트 (+, -)
no = True       # 불가능할 경우, if문 사용을 위한 boolean

# n 크기만큼 for문
for _ in range(n):
    order = int(sys.stdin.readline())

    while count < order:    # count가 order보다 작을 경우
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == order:  # stack 리스트의 끝 부분과 order가 같으면
        stack.pop()
        result.append('-')
    else:
        no = False
        break

if no == False:             # stack 리스트의 끝 부분과 order가 같지 않으면
    print("NO")
else:
    for i in result:
        print(i)
