N = int(input())
lst = []

for _ in range(N):
    lst.append(input())

set_list = set(lst)
lst = list(set_list)

lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)