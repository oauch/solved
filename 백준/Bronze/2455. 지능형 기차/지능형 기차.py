result_list = []
result = 0

for i in range(4):
    a, b = map(int, input().split())
    result += b
    result -= a
    result_list.append(result)

print(max(result_list))