
def NbrePossiblites(n):
    r = []
    if n > 12 or n < 1:
        print('c\'est impossible de faire cette somme')
    faces = [1,2,3,4,5,6]
    for face in faces:
        if (not 1<=n-face<=6 ): continue
        r.append((face,n-face))
    print(f'il y a {len(r)} facon(s) de faire {n} avec deux des')
    possiblites = 'Les possibilites : '
    for i in range(len(r)): 
        possiblite = r[i]
        possiblites += str(possiblite)
        if ( not i == len(r) - 1):
            possiblites += ' ;'
    print(possiblites)
NbrePossiblites(6)
