def palind_rec(ch,i=0):
    if (i >= len(ch)//2):
        return True
    if (ch[i] != ch[len(ch)-1-i]):
        return False
    return palind_rec(ch,i+1)
print(palind_rec("maram"))
