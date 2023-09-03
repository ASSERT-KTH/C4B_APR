x,y,z=map(int,input().split())
print(min((x+y+z),2*(x+y),2*(y+z),2*(x+z)))