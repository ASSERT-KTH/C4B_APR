s = input() ;
l=len(s);
new=s[::-1];
i=0;
count=0;
while(i<l):
    if (new[i] != s[i]):
        count=count+1;
    i=i+1;
if (count==1):
    print('Yes');
elif(count>1):
    print('No');
else:
    if(l%2==0):
        print('NO');
    else:
        print('Yes');