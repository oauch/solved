N = int(input())
a = list(map(int, input().split()))

count = 0
result = 0

for i in range(N):
    if a[i] == 1:
        count += 1
        result += count
    else:
        count = 0

print(result)