line=input()
result=0
maxi=1
for x in range(1,len(line)):
    if line[x]==line[x-1]:
        maxi+=1
        if maxi>result:
            result=maxi
    else:
        if maxi>result:
            result=maxi
        maxi=1
if result>=7:
    print ("YES")
else:
    print ('NO')