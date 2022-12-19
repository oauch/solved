n = int(input())
a = list(map(int, input().split()))
count = 0

for i in a:
    if i == 0 or i == 1:
        continue
    else:
        sosu = True
        for j in range(2, i):
            if i % j == 0:
                sosu = False
        if sosu == True:
            count += 1    


print(count)