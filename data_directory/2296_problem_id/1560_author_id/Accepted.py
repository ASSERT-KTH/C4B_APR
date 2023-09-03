a=input()
b=a.split()

if int(b[0])%2==1 and int(b[1])%2==1:
     print(int((int(b[0])*int(b[1])-1)/2))

else:
    print(int(int(b[0])*int(b[1])/2))