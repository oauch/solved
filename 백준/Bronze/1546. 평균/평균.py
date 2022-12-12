n = int(input())
b = list(map(int, input().split()))

one_step = 0
result = 0
max_num = max(b)

# 새로운 성적계산법
for i in range(len(b)):
    b[i] = b[i] / max_num * 100

# 성적모두 더하기
for j in range(len(b)):
    result += b[j]

# 성적 평균구하기
a = result / n
print(a)