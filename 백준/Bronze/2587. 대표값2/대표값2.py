a_list = []
for i in range(5):
    a_list.append(int(input()))

result = 0
for i in a_list:
    result += i
print(result // len(a_list))

a_list.sort()
print(a_list[len(a_list) // 2])