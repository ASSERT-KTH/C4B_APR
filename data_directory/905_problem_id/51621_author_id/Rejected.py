s = input()
#list = s.split()
n = int(s.split()[0])
m = int(s.split()[1])
k = int( s.split()[2])
count =0
for i in range(1,n+1):
    for j in range(1,m+1):
        count+=2
        if(count == k):
            print("%d %d R"%(i,j))
        elif (count == k+1):
            print("%d %d L" % (i, j))