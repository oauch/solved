L = int(input()) # 방학일수
A = int(input()) # 국어 
B = int(input()) # 수학
C = int(input()) # 국어 최대 페이지
D = int(input()) # 수학 최대 페이지

Kor, Math = 0, 0
count = 0

while 1:
    if A >= C or B >= D:
        Kor += C
        Math += D
        count += 1
    if A <= Kor and B <= Math:
        print(L - count)
        break