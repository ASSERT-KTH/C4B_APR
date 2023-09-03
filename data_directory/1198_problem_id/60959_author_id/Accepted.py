a = input()
arr = ['H', 'Q', '9']
narr = []
for i in range (len(arr)):
    if arr[i] in a:
        narr.append("YES")
    else:
        narr.append('NO')
#print(narr)
if 'YES' in narr:
    print('YES')
else:
    print('NO')