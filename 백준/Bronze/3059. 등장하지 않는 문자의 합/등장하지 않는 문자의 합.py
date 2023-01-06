t = int(input())

asc = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

for _ in range(t):
    a = set(input())
    sum = 0
    result = asc - a

    for i in result:
        sum += ord(i)
    print(sum)