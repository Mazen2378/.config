def saisir():
    global n
    n = int(input('donner nombre '))
    if (n < 0):
        n = saisir()
    return n
n = saisir()
def produitChiffres(n,r=1):
    if (n==0 ): return r
    r *= (n%10)
    return produitChiffres(n//10,r)

def Persistance(num,r=0):
    newNum = produitChiffres(num)
    r += 1
    if (newNum // 10 == 0):
        return r
    return Persistance(newNum,r)

print(Persistance(n))
