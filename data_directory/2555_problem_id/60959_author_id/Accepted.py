a = input()
arr = []
if len(a) >= 7:
    for i in range (len(a)-6):
        b = a[i:i+7]
        #print(b)
        #print('set',set(b))
        #print('len(set)',len(set(b)))
        if len(set(b)) == 1:
            arr.append("YES")
        else:
            arr.append("NO")
#print(arr)
if "YES" in arr:
    print("YES")
else:
     print("NO")