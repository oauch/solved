n = int(input())
a = list(map(int, input().split()))
count = 0

for i in a:
    if i == 0 or i == 1:
        continue
    else:
        # 소수 판별 Boolean
        sosu = True
        # 소수 비교를 위한 for문
        for j in range(2, i):
            # 0으로 나뉘어 떨어지면 소수가 아님
            if i % j == 0:
                sosu = False    # False를 주어 밑에 if문 못들어가서 카운트 안됨
        # 소수이면 카운트
        if sosu == True:
            count += 1    


print(count)