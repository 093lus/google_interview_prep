def rotate_array_without_extra_space(l):
    half_len = len(l)//2
    for i in range(0,half_len):
        temp = l[i]
        l[i] = l[len(l)-i-1]
        l[len(l)-i-1] = temp
    return l


print(rotate_array_without_extra_space([1,2,8,5,7]))