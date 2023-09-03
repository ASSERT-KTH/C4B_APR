table=["1/1","5/6","2/3","1/2","1/3","1/6"]
a,b=map(int,input().split())
print(table[6-max(a,b)+1])