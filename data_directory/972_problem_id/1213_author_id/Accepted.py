a,b = input().split()
a,b = int(a),int(b)
if abs(a-b)>1 or (a ==0 and b ==0):
    print('NO')
else:
    print('YES')