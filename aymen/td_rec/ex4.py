def comb_rec(p,n):
    if p == 0 or p == n:
        return 1
    else :
        return comb_rec(p,n-1) + comb_rec(p-1,n-1)
print(comb_rec(2,4))
