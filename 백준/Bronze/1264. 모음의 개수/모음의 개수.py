abc_list = ['a', 'e', 'i', 'o', 'u']
a_list = []

while 1:
    a = input().lower()
    if a == '#':
        break
    a_list.append(a)
    for i in a_list:
        count = 0
        for j in i:
            if j in abc_list:
                count += 1
            else:
                continue
    print(count)