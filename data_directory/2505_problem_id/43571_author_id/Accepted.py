a,b = input().split(" ")
a,b = int(a),int(b)
c=a-b
if(a%c == 0 and b%c == 0):
    print("Equal")
elif(a>b):
    print("Masha")
else:
    print("Dasha")