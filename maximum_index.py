def max_index_range(arr):
    res = len(arr)-1
    while res:
        for i in range(len(arr)):
            if i + res > len(arr) - 1:
                break
            if arr[i] < arr[i + res]:
                return res

        res-=1
    return res

print(max_index_range([34 ,8 ,10 ,3 ,2 ,80 ,30 ,33 ,1]))
