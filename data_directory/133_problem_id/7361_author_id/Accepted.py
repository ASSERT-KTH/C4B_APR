'''
Created on 2016年3月19日

@author: HaoGe
'''
start = list(map(int, input().split()))
end = list(map(int, input().split()))
mylist=[]
for i in range(3):
    if start[i]<end[i]:
        end[i]-=start[i]
        start[i]=0
    else:
        start[i]-=end[i]
        end[i]=0
    mylist.append([start[i],end[i]])
mylist.sort(key=lambda my:my[0], reverse=True)
i=0 #初始剩余资源
j=0 #目标资源量
while j<3 and i<3:
    while mylist[j][1]>0 and i<3:
        if mylist[i][0]<=mylist[j][1]*2:
            mylist[j][1]-=mylist[i][0]//2
            i+=1
        else:
            mylist[i][0]-=mylist[j][1]*2
            mylist[j][1]=0
    j+=1
if mylist[2][1]+mylist[1][1]+mylist[0][1]>0:
    print("No")
else:
    print("Yes")