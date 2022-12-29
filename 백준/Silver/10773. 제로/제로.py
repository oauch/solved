import sys

K = int(sys.stdin.readline())
stack = []
result = 0

for _ in range(K):
    A = int(sys.stdin.readline())

    # 0인 경우, 가장 최근의 쓴 수 삭제
    if A == 0:
        stack.pop()
    # 그렇지 않으면, 스택에 추가
    else:
        stack.append(A)

print(sum(stack))