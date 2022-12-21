n = int(input())

a_list = []
for i in range(n):
    a = input()
    a_list.append(a)

if a_list.count('1') > a_list.count('0'):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")