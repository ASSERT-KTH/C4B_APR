n=int(input())
for i in range(n+1,10000):
    if len({int(j) for j in ' '.join(str(i)).split()})==4:
        print(i)
        break