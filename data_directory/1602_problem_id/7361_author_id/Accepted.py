from itertools import product
x, t,a,b,da,db = map(int, input().split())
ans=0
la,lb = [0],[0]
for i in range(t):
    la +=[a-i*da]
    lb +=[b-i*db]
for sx in product(la,lb):
    if sx[0]+sx[1]==x:
        ans=1
        break
print(['NO','YES'][ans])