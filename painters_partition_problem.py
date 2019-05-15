import math

def painters_partition_problem(k, n, arr):
    if k==1:
        return sum(arr)
    max_time = math.inf
    diff = math.inf
    for i in range(1,n):
        time =  sum(arr[:i])

        others_time = painters_partition_problem(k-1,n-i,arr[i:])
        time_diff = abs(others_time-time)
        min_time_diff = min(diff,time_diff)
        if min_time_diff< diff:
            diff = min_time_diff
            max_time = max(time, others_time)
    return max_time


print(painters_partition_problem(3,6,[10, 20, 60, 50, 30, 40 ]))