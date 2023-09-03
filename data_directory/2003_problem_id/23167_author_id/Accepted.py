n = int(input())
for i in range(n+1, 10000):
    if len(set(str(i)))==len(str(i)):
        print(i)
        break