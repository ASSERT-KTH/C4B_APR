n=int(input())
s=input()
s1=0
s2=0
for i in range(n//2):
    if s[i]!=s[n-i-1]:
        import sys
        print('NO')
        sys.exit(0)
print ('YES')