#!usr/bin/python 3

#def func (string, x, let):
 #   for y in range(x,

def main():
    s=input()
    previous=' '
    h=s.find('h')
    e,l1,l2,o=0,0,0,0
    for y in range(h,len(s)):
        if s[y]=='e':
            e=y
            break
    for y in range(e,len(s)):
        if s[y]=='l':
            l1=y
            break
    for y in range(l1,len(s)):
        if s[y]=='l':
            l2=y
            break
    for y in range(l2,len(s)):
        if s[y]=='o':
            o=y
            break
    #print(h,e,l1,l2,o)
    if e==0 or l1==0 or l2==0 or o==0: print('NO')
    else: print('YES')

if __name__=='__main__':
    main()