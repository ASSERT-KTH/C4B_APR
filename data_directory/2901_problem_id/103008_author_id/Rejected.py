inp=input().split()
c=int(inp[0]) #length of the book in page
v0=int(inp[1]) # initial reading spead
v1=int(inp[2])  #max reading spead
a=int(inp[3]) #acceleration in reading speed
l=int(inp[4]) #number of pages of rereading

nbpagerest=c
day=0
while nbpagerest>0:
    if day>0:
        nbpagerest=nbpagerest+l
        
    if day*a<=v1:
        nbpagerest=nbpagerest-v0-day*a
    else:
        nbpagerest=nbpagerest-v1
    day=day+1

print(day)