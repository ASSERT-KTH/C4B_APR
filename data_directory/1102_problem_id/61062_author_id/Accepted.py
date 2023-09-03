s=input()
ans=""
l=['a','e','i','o','u','y','Y','A','E','I','O','U']
for i in s:
    if(i not in l):
        ans=ans+"."+i.lower()
print(ans)