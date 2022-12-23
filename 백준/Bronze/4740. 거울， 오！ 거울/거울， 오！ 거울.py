a_list = []

while 1:
    a = input()
    if a == '***':
        break
    a_list.append(a[::-1])

for i in a_list:
    print(i)