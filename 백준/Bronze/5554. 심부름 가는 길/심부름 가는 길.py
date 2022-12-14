A = int(input()) # 집 -> 학교 이동시간
B = int(input()) # 학교 -> 피시방 이동시간
C = int(input()) # 피시방 -> 학원 이동시간
D = int(input()) # 학원 -> 집 이동시간

print((A+B+C+D) // 60)
print((A+B+C+D) % 60)