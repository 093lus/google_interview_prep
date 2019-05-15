def drop_egg(n,k):
    if k ==1:
        return n
    m = n
    if n==0:
        return 0
    if n==1:
        return 1
    for i in range(1,n+1):
        drop=max(drop_egg(i-1,k-1),drop_egg(n-i-1,k))
        m=min(drop,m)
    return m+1

print(drop_egg(10,2))