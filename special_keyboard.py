def max_a_count(n):
    if n<=3:
        return n
    return max(max_a_count())