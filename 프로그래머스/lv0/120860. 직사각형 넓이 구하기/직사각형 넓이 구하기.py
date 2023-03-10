def solution(dots):
    a = []
    b = []

    for i in dots:
        a.append(i[0])
        b.append(i[1])
    resultA = max(a) - min(a)
    resultB = max(b) - min(b)
    
    return resultA * resultB
    