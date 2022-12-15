n, m = map(int, input().split())

if m in (1, 2):
    print('NEWBIE!')
elif n >= m and m not in (1, 2):
    print('OLDBIE!')
else:
    print('TLE!')