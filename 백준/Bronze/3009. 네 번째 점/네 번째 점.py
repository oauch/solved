a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

x_list = [a1, b1, c1]
x_list.sort()
y_list = [a2, b2, c2]
y_list.sort()

if x_list[0] == x_list[1]:
    print(x_list[2], end=' ')
else:
    print(x_list[0], end=' ')

if y_list[0] == y_list[1]:
    print(y_list[2])
else:
    print(y_list[0])