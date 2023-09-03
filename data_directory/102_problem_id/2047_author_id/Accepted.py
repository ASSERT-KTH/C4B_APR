x,y,z = map(int,input().split())

if(x+y <= z):
    print(x*2 + y*2)
elif(x == y == z):
    print(x*3)
elif(x > y and x > z):
    print(y*2 + z*2)
elif(y > x and y > z):
    print(x*2 + z*2)
else:
    print(x+y+z)