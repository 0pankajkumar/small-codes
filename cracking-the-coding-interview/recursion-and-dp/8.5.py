# Recursively Multiply


# Brute force
def multipy(a, b):
    if b <= 1:
        return a
    else:
        return a + multipy(a, b-1)

ans = multipy(25,3)
print(ans)







# Optimized memoized
def multipy(a, b):
    if b <= 1:
        return a
    else:
        return a + multipy(a, b-1)

ans = multipy(25,3)
print(ans)
