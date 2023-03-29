def ajouter_note(r,mat,note):
    r[mat].append(note)
def moy_matiere(r,mat):
    l = r[mat]
    s = 0 
    for i in l:
        s += i
    print(s)
    return s / len(l)
def moy_generale(r):
    s = 0
    for key in r.keys():
        s += moy_matiere(r,key)
    return s / len(r.keys())
def meilleru_note(r):
    res = [] 
    maximum = 0
    for key,value in r.items():
        for i in value:
            if i == maximum :
                res.append(key) 
            elif i > maximum:
                maximum = i
                res = [key] 
    return (maximum,res)

def meilleru_moyen(r):
    res = [] 
    maximum = 0
    for key in r.keys():
        moyen = moy_matiere(r,key)
        if moyen == maximum :
            res.append(key) 
        elif moyen > maximum:
            maximum = moyen
            res = [key] 
    return (maximum,res)
r = {'maths':[14,8.5,12],'physique':[20,17,14],'anglais':[13,8,10,9.5]} 
print(meilleru_moyen(r))


