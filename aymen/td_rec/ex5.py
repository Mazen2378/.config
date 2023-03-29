def suite_rec1(n):
    if n == 0:
        return 2
    prev = suite_rec1(n-1)
    return (prev + 2 / prev) / 2
def suite_rec2(n):
    if n == 0:
        return 2
    return (suite_rec2(n-1) + 2 / suite_rec2(n-1)) / 2
n = 182 
print(suite_rec1(n), ' ', suite_rec2(n))
