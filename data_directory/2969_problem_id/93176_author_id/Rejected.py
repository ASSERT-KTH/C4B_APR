l = list(int(i) for i in input().split())
if (l[0]/l[1])+2*l[3]==(l[0]/l[2])+2*l[4]:
    print ("Friendship")
elif (l[0]/l[1])+2*l[3]>(l[0]/l[2])+2*l[4]:
    print ("First")
elif (l[0]/l[1])+2*l[3]<(l[0]/l[2])+2*l[4]:
    print ("Second")