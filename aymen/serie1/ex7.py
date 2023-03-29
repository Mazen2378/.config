def saisir():
    global n
    n = int(input('donner nombre '))
    if (n < 0):
        n = saisir()
    return n

res = 0
def russe(multiplicateur,multiplicande):
    global res
    if multiplicateur % 2 == 1:
        res += multiplicande
    if multiplicateur == 1:
        return res
    return russe(multiplicateur // 2,multiplicande * 2)

print(russe(saisir(),saisir()))
