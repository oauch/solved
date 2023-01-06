a = int(input())

order = list(map(int, input().split()))
order.sort()

print(order[-1])