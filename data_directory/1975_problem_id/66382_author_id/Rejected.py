n,t=map(int,input().split())
s=input()
s=list(s)
i=0
for z in range(t):
    while(i<len(s)-1):
        if(s[i]=="B" and s[i+1]=="G"):
            s[i]="G"
            s[i+1]="B"
            i=i+2
        else:
            i=i+1
for i in range(len(s)):
    print(s[i],end='')