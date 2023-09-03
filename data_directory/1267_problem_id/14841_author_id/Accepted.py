n=int(input())
s=input()
s1=0
s2=0
for i in range(n//2):
    if s[i]!='7' and s[i]!='4':
        import sys
        print ('NO')
        sys.exit(0)
    s1+=ord(s[i])-48
for i in range(n//2,n):
    if s[i]!='7' and s[i]!='4':
        import sys
        print ('NO')
        sys.exit(0)    
    s2+=ord(s[i])-48
if s1==s2:
    print ('YES')
else:
    print ('NO')