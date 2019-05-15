def quick_sort(arr):
    if len(arr)<=1:
        return
    piv = arr[0]
    pos = 0
    n=len(arr)-1
    for i in range(len(arr)):
        if arr[i]<piv:
            pos+=1
            arr[i],arr[pos]=arr[pos],arr[i]

    arr[pos],arr[0] = arr[0],arr[pos]
    quick_sort(arr[0:pos])
    quick_sort(arr[pos+1:])

l =  [4,7,9,1,3,2,65,6]
quick_sort(l)
print(l)

# l = [1,2,3]
# print(l[1:])