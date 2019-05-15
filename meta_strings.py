def meta_strings(str1, str2):
    if len(str1) != len(str2):
        return 0
    first_index = 0
    dismatch_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if not dismatch_count:
               first_index = i
            dismatch_count += 1
            if dismatch_count == 2:
                if str1[first_index] != str2[i] or str2[first_index] != str1[i]:
                    return 0
                else:
                    dismatch_count = 0
    if dismatch_count > 0:
        return 0
    return 1


print(meta_strings("geeks" , "keegs"))
print(meta_strings("rsting" , "string"))