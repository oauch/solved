t = int(input())
list_a = []
for _ in range(t):
    a = input()
    list_a.append(a)

for i in list_a:
    print(i[0]+i[-1])