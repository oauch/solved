a = input().split()
b = []
# 입력받은 값 뒤집기
for i in a:
    b.append(i[::-1])
# 뒤집은 값중 최댓값
print(max(b))    