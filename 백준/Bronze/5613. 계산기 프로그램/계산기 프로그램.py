# 처음 숫자는 무조건 정수형이기 때문에
# 정수형으로 하나 입력하고 시작
first = int(input())

while 1:
    # 부호 입력
    a = input()
    # 만약 = 이 나오면 반복문 종료
    if a == '=':
        break
    # 숫자 입력
    n = int(input())
    # 사칙연산
    if a == '+':
        first += n
    elif a == '-':
        first -= n
    elif a == '*':
        first *= n
    else:
        first //= n
print(first)