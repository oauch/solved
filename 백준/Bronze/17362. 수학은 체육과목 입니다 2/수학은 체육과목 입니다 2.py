n = int(input())

m = n % 8

if m == 1 :
    print(1)
elif m in [2, 0]:
    print(2)
elif m in [3, 7]:
    print(3)
elif m in [4, 6]:
    print(4)
elif m == 5:
    print(5)