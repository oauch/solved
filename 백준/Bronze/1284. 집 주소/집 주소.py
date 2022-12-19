count = 0
while 1:
    a = input()
    # 양옆 / 공백 카운트
    count = len(a) + 1
    # a가 0일때는 반복 멈춤
    if a == '0':
        break
    # a의 숫자만큼 반복문
    for i in a:
        # 만약 1이면 2개 카운트
        if i == '1':
            count += 2
        # 0이면 4개 카운트
        elif i == '0':
            count += 4
        # 나머지는 3개 카운트
        else:
            count += 3
    print(count)