print(sum(abs(x-3)+abs(y-3)for x in range(5) for y,v in enumerate(input().split()) if int(v)))