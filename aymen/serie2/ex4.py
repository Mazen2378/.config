L = [[2,55],[-5,15],[1,1],[-1,0]]

def AffPol(L): 
    res = ''
    for [a,n] in L:
        if n == 0:
            res += f'{a}'
        elif n == 1:
            if a > 0 and res != '' : res += '+'
            res += f'{a}X'
        else:
            if a > 0 and res != '' : res += '+'
            res += f'{a}X^{n}'
    print(res)

AffPol(L)

def EvPol(L,x0):
    res = 0
    for [a,n] in L:
        res += a*(x0)**n
    print(res)


EvPol([[-5,2],[6,1],[2,0]],2)

def MtPol(L,a,n):
    for i in range(len(L)):
        [a0,n0] = L[i]
        L[i] = [a*a0,n+n0] 
    print(L)
    return L


MtPol([[-5,2],[6,1],[2,0]],2,5)
def AddPol(L,a,n):
    L.insert(0,[a,n])
    print(L)
    return L


AddPol([[-5,2],[6,1],[2,0]],2,5)
