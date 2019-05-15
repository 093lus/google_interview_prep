def word_break(input, list):
    i = 0
    j = 0
    while i <= len(input):
       if input[j:i+1] in list:
           j=i+1
           i+=1
           if j>= len(input):
               return True
       else:
           i+=1
    return False



print(word_break('iilike', ['i', 'like', 'sam']))
