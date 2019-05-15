def allocate(arr,m):
    st_pages = [0]*m
    n = len(arr)
    i = 0
    j = 0
    sign = 1
    while i<n:
        while j<m and i<n:

            st_pages[j]+=arr[i]
            j += sign
            i+=1
        else:
            sign = -sign

    print(max(st_pages))

allocate([90,67,34,12],2)