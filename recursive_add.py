def recurse_add(m,n):
    if n<1:
        return m
    return recurse_add(m+1,n-1)

m = 1
n = 6
print("%d + %d = %d" % (m,n,recurse_add(m,n)))