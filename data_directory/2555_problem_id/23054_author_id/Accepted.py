string = str(input())
ones = "1111111"
zeroes = "0000000"
string=string+'2'
total = 1
for i in range(len(string)-7):
    if(string[i:i+7]==ones) or (string[i:i+7]==zeroes):
        total = total * 0
    else:
        total = total + 0
if(total==0):
    print ("YES")
else:
    print ("NO")