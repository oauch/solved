A = list(map(int, input().split())) # 민국의 점수
B = list(map(int, input().split())) # 만세의 점수

A_result = 0
B_result = 0

for i in A:         # 민국의 점수합
    A_result += i

for i in B:         # 만세의 점수합
    B_result += i

if A_result == B_result:    #점수합이 같을때, 민국의 점수
    print(A_result)
elif A_result > B_result:   #민국이 점수 더 클때
    print(A_result)
else:                       #만세가 점수 더 클때
    print(B_result)