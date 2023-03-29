V = ['a','o','u','e','i','y','w']

def voy(c): return c in V 
def compte_voy(phr):
    res = 0
    for i in phr:
        if voy(i): 
            res += 1
    return res

def distance_hamming(ch1,ch2):
    res = 0
    for i in range(len(ch1)):
        if ch1[i] != ch2[i]:
            res += 1
    return res

def sup_occ (ch,c):
    res = []
    for i in ch:
        if i != c:
            res.append(i)
    return ''.join(res)
print(sup_occ('MPAPPC','P'))
