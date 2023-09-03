n=int(input())
for i in range(n+1,1000):
    if len({int(j) for j in ' '.join(str(i)).split()})==4:
        print(i)
        break