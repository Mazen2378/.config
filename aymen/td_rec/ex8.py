#1
def tailleListe(L,i=0):
    if i == len(L):
        return i
    return tailleListe(L,i+1)
print(tailleListe([1,4,8,5,2]))

def sommeListe(L,i=0):
    if i == len(L) - 1:
        return L[i]
    return L[i] +  sommeListe(L,i+1)
print(sommeListe([1,4,8,5,2]))


def affListe(L,i=0):
    print(L[i])
    if i == len(L) - 1:
        return
    affListe(L,i+1)
affListe([1,4,8,5,2])

def affListeInv(L,i=0):
    if i == len(L) - 1:
        print(L[i])
        return
    affListeInv(L,i+1)
    print(L[i])
affListeInv([1,4,8,5,2])
