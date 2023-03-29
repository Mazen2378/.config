def copie_rec(ch,res=''):
    if res == ch:
        return res
    return copie_rec(ch,res+ch[len(res)])
print(copie_rec("mazen"))
