# 과자 한개 가격 k
# 사려고하는 과자 갯수 n
# 현재 가진 돈의 액수 m

k, n, m = map(int, input().split())

if k * n > m:    
    print((k * n) - m)
else:
    print(0)