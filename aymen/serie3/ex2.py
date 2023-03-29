def occ_couleurs(d,c):
    r = 0
    for value in d.values():
        if value == c:
            r += 1
    return r
def dict_long_couleur(d):
    dict = {}
    for key in d.values():
        dict[key] = len(key)
    return dict 

def max_long_couleur(d):
    res = []
    maximum = 0
    dict = dict_long_couleur(d)
    for key,value in dict.items():
        if value == maximum :
            res.append(key)
        elif value > maximum:
            maximum = value
            res = [key] 
    return res
print(max_long_couleur({4:'blue',1:'black',3:'green',2:'black'}))
