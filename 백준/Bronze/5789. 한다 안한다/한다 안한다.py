N = int(input())

for _ in range(N):
    a = input()
    
    half_len = int(len(a) / 2)

    if a[half_len - 1] == a[half_len]:
        print("Do-it")
    else:
        print("Do-it-Not")