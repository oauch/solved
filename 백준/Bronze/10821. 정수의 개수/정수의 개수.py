int_a = []
a = input().split(',')
count = 0

for i in a:
    int_a.append(int(i))

for i in int_a:
    if type(int(i)):
        count += 1
    else:
        continue

print(count)