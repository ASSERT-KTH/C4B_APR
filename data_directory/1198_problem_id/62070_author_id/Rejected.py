p=input()
for i in range(len(p)):
    if p[i]=='H' or p[i]=='Q' or p[i]=='+' or p[i]=='9':
        print('YES')
        exit(0)
print('NO')