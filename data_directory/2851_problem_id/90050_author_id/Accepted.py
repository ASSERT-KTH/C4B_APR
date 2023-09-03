def bin_search(calc, n):
    hi = n + 1
    lo = ans = 0
    while (hi - lo) > 1:
        mid = (hi + lo) // 2
        if calc(mid) <= n:
            lo = ans = mid
        else:
            hi = mid
    return ans


[vl, va] = [int(x) for x in input().split()]
[vl, va] = [bin_search(lambda x: x * x, vl), bin_search(lambda x: x * (x + 1), va)]
print('Valera') if vl > va else print('Vladik')