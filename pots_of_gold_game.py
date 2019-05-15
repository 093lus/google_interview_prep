def gold_game(arr,s,e):
    if e-s<2:
        return max(arr[s:e+1])

    sol1 = arr[s]+ min(gold_game(arr,s+2,e),gold_game(arr,s+1,e-1))
    sol2 = arr[e] + min(gold_game(arr, s , e-2),gold_game(arr, s +1, e- 1))
    return  max(sol1,sol2)

print(gold_game([8,15,3,7],0,3))