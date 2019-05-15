import math

def traveling_salesman_problem(mat, index):
    no_way = True
    for j in range(len(mat)):
        if mat[index][j] > 0:
            no_way = False
    if no_way:
        return 0
    s  = math.inf
    l = math.inf
    n = len(mat)
    for j in range(n):
        if mat[index][j] > 0:
            lst=[]
            val = mat[index][j]
            for i in range(n):
                lst.append(mat[i][j])
                mat[i][j] = 0
            l = traveling_salesman_problem(mat, j) + val
            for i in range(n):
                mat[i][j] = lst[i]
            s = min(l, s)
    return s

l = [[0,1000,5000],[5000,0,1000],[1000,5000,0]]
print(traveling_salesman_problem(l,0))
