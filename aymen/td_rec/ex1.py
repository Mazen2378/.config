def pgcd_rec(a,b):
    if b == a:
        return a
    elif a > b:
        return pgcd_rec(a-b,a)
    else:
        return pgcd_rec(a,b-a)
print(pgcd_rec(18,51))

