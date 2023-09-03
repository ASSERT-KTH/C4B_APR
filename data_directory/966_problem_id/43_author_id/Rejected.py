import sys
beds,pillows,frodo=map(int,sys.stdin.readline().split())
pillows=pillows-beds-1 
layer=2
while pillows>0:
    if beds==1:
        layer=pillows+2
        pillows=0
        break
    if frodo-1<layer-1 and beds-frodo<layer-1:
        layer+=(int(pillows/(beds-1))+1)
        break
    else:
        pillows-=(min(frodo-1,layer-1)+min(layer-1,beds-frodo))
    if pillows>0:
        pillows-=1
    layer+=1   
if pillows==0:
    print(layer)
else:
    print(layer-1)