def get_int():
    return map(int, input().split())

t, s, x = get_int()

print(['NO', 'YES'][((((x-t)/s) == ((x-t)//s)) or (((x-t-1)//s) > 0 and (((x-t-1)/s) == ((x-t-1)//s)))) and x >= t])