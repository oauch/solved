a = input().upper() # a를 모두 대문자로 만들어줌
b = list(set(a))    # a에서 중복 없앰

cnt = 0
chr = ''

for i in range(len(b)):
    # 문자열 a안에서 찾고 싶은 문자의 갯수 찾음
    n = a.count(b[i])

    # 만약 cnt보다 n이 더 크면(카운트가 되면)
    if cnt < n:
        cnt = n
        chr = b[i]
    # 그렇지 않고 같은 값이면
    elif cnt == n:
        chr = '?'

print(chr)