#problem 705A
number=int(input())
x=""
for i in range (0,number):
 x=x.replace("it","that")
 if i%2==0:
   x+=" I hate it"
 if i%2==1:
   x=x.replace("it","that")
   x+=" I love it"
print(x)