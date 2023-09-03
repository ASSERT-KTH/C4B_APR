a = input()
arr = []
if len(a) >= 7:
    for i in range (len(a)-7):
        b = a[i:i+7]
        #print('set',set(b))
        #print('len(set)',len(set(b)))
        if len(set(b)) == 1:
            arr.append("YES")
        else:
            arr.append("NO")
if "YES" in arr:
    print("YES")
else:
     print("NO")