def frequences(str):
    mot = ''
    dict = {} 
    for i in str:
        if i == ' ' and mot != '':

            dict[mot] = dict.get(mot,0) +1
            mot = ''
        else:
            mot += i
    if mot != '':
        dict[mot] = dict.get(mot,0) +1
    return dict


def plus_frequents(str):
    res = ''
    maximum = 0
    dict = frequences(str)
    for key,value in dict.items():
        if value == maximum :
            res += key + ' '
        elif value > maximum:
            maximum = value
            res = key + ' ' 
    return res
print(plus_frequents('do do mazen mazen mi fa jjj do jjj a jjj'))
