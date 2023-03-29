def somme_rec(n):
    if n == 0:
        return 0
    return somme_rec(n-1) + n*n

print(somme_rec(3))
