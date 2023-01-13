n=int(input())
x=list(map(int,input().split()))
x2=list(set(x))
x2.sort()
for i in range(len(x2)):
    print(x2[i], end=' ')
