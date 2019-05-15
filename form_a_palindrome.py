def form_pal(str):
    l =len(str)
    if(l==1 or(l==2 and str[0]==str[1])):
        return 0
    for i in range(l):
        if str[i]!=str[l-i-1]:

            beg = form_pal(str[i:l-i-1])
            end = form_pal(str[i+1:l-i])
            if beg>=end:
                return end+1
            else:
                return beg+1
        else:
            return form_pal(str[i+1:l-i-1])


print(form_pal('geeks'))