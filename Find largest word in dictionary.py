def largest_word(w_list, w_string):
    max = ''
    for w in w_list:
        j = 0
        k = 0

        for k, val in enumerate(w):


            while w[k] != w_string[j]:
                # j += 1
                if j >= len(w_string) - 1:
                    break
                j += 1
            else:
                if k == len(w) - 1:
                    if len(w) > len(max):
                        max = w
                    break
                j += 1

    return max


print(largest_word(["ale", "apple", "monkey", "plea"], "abpcplea" ))
print(largest_word(["pintu", "geeksfor", "geeksgeeks", " forgeek"], "geeksforgeeks"))
