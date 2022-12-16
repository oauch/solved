a = input()

while a != '0':
    a_list = list(a)
    a_list.reverse()
    a_reverse = ''.join(a_list)

    if a == a_reverse:
        print('yes')
    else:
        print('no')
    a = input()