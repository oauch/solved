n, w, h, l = map(int, input().split())

garo = w // l
saro = h // l
result = garo * saro

print(min(n, result))