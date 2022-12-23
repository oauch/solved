while True:
    try:
        a = list(input())
        so, da, su, sp = 0, 0, 0, 0
        for i in a:
            if i.islower():
                so += 1
            elif i.isupper():
                da += 1
            elif i.isdigit():
                su += 1
            elif i.isspace():
                sp += 1
        print("{} {} {} {}".format(so, da, su, sp))
    except EOFError:
        break