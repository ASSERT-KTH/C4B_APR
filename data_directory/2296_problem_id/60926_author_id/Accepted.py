lisa= input()
index=0
for i in range(len(lisa)):
    if(lisa[i]==" "):
        index=i

print(int((int(lisa[0:index])*int(lisa[index+1:len(lisa)]))/2))