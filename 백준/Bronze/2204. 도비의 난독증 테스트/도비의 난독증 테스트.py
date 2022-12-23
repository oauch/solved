while 1:
    abc = []
    a = int(input())
    if a == 0:
        break
    for i in range(a):
        abc.append(input())
    abc.sort(key=str.lower)
    print(abc[0])