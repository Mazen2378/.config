def rec_chiffre(n):
    u = n % 10
    if u == n:
        return n
    return rec_chiffre(n//10) + u
print(rec_chiffre(218))
