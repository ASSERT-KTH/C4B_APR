s=str(input())
chk1,chk2 = '000000','111111'
if (s.find(chk1) >= 0 or s.find(chk2) >= 0):
    print("YES")
else:
    print("NO")