a=int(input())
for _ in range(a):
    R,S=input().split()
    for i in range(len(S)):
        print(S[i]*int(R),end='')
    print()