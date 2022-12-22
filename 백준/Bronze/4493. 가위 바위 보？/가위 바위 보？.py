t = int(input())

for _ in range(t):
    n = int(input())
    a_count = 0
    b_count = 0
    for i in range(n):
        a, b = input().split()
        if a == 'R' and b == 'S' or a == 'S' and b == 'P' or a == 'P' and b == 'R':
            a_count += 1
        elif a == b:
            a_count +=1
            b_count +=1
        else:
            b_count += 1
    
    if a_count > b_count:
        print("Player 1")
    elif a_count == b_count:
        print("TIE")
    else:
        print("Player 2")