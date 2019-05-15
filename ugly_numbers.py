def ugly_number(n):
    output=None
    num = 0
    i = 1
    while n>0:
        j = i
        while True:
            if j==1:
                n-=1
                output = i
                break
            if j%2==0:
                j = j/2
            elif j%3==0:
                j = j/3
            elif j%5==0:
                j = j/5
            else:
                break
        i+=1

    return output

print(ugly_number(4))