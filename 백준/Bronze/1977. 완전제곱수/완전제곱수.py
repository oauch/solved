m = int(input())
n = int(input())
result_li = []
result = 0

for i in range(m , n+1):
    if i ** 0.5 == round(i**0.5, 1):
        result_li.append(int(i))
    else:
        continue

if len(result_li):
    for i in result_li:
        result += i
    print(result)
    print(min(result_li))        
else:
    print(-1)