
def suite(n):
    if n == 1: return 4
    if n == 2: return 2
    if n == 3: return 1
    return (2*suite(n-3)+suite(n-1))**0.5 + suite(n-2)

print(suite(1))
