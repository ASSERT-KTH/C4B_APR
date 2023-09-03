beds,pillows,frodo=map(int,input().split())
flag=0
if beds==pillows:
    flag=1
pillows=pillows-beds-1
layer=2
while pillows>0:
    if beds==1:
        layer=pillows+2
        pillows=0
        break
    if frodo-1<layer-1 and beds-frodo<layer-1:
        layer+=(int(pillows/(beds))+1)
        break
    else:
        pillows-=(min(frodo-1,layer-1)+min(layer-1,beds-frodo))     
    pillows-=1
    if pillows<0:
        layer-=1      
    layer+=1
if flag==1:
    print('1')
elif pillows<0:
    print(layer)
elif pillows==0:
    print(layer)
else:
    print(layer-1)