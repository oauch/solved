taro = 1000
ang = [500, 100, 50, 10, 5, 1]
count = 0

a = int(input())
result = taro - a

for i in ang:
    while i <= result:
        result -= i
        count += 1
print(count)