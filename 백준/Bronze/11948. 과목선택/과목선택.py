A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

A_GROUP = [A, B, C, D]
B_GROUP = [E, F]
final = []
result = 0

# 4과목중 가장 점수가 높은 3과목 선택
for i in range(3):
    final.append(max(A_GROUP))
    A_GROUP.remove(max(A_GROUP))

# 2과목중 가장 높은 점수 과목 선택
final.append(max(B_GROUP))

# 그 값들 모두 더하기
for i in final:
    result += i
print(result)