while 1:
    a = list(map(int, input().split()))
    max_num = max(a)
    a.remove(max(a))
    if 0 in a:
        break
    elif a[0] * a[0] + a[1] * a[1] == max_num * max_num:
        print('right')
    else:
        print('wrong')