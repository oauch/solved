while 1:    
    a = input().split()
    if a[0] == '#' and a[1] == '0' and a[2] == '0':
        break
    if a[1] > '17' or a[2] >= '80':
        print(a[0] + ' Senior')
    else:
        print(a[0] + ' Junior')