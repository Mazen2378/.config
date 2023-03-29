L = [1,1,1,1,2,1,1,1,1,1,2]
def VerifPalindrome(L,pos,lg) :
    coup = L[pos:lg+pos]
    if len(coup) != lg: return False
    print(coup)
    for i in range(len(coup)//2+1):
        if coup[i] == coup[len(coup)-1-i]:
            continue
        else:
            return False

    return True

def Palindrome7(L): 
    res = 0
    for i in range(len(L)):
        if (VerifPalindrome(L,i,7)):
            res +=1

    return res


def PalindromePos(L,n): 
    for i in range(len(L)):
        if (VerifPalindrome(L,i,n)):
            return i

    return False

print(PalindromePos(L,7))
