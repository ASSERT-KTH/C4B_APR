call, performance, day = (int(x) for x in input().split())
calls_per_day = [n * call for n in range(1,day + 1)]
performances_per_day = [n * performance for n in range(1, day + 1)]
ans = 0
for acall in calls_per_day:
    if acall <= day:
        for aperformance in performances_per_day:
            if aperformance <= day and aperformance == acall:
                ans += 1     
print(ans)