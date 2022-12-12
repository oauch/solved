a = int(input())

for _ in range(a):
    OX = input()
    sum = 0
    k = 0
    
    for i in OX:
        if i == 'O':
            k += 1
            sum += k
        else:
            k = 0
    print(sum)