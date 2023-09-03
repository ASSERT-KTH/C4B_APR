a = input()
a = a.split();
for i in range(3) :
    a[i] = int(a[i])
if a[2] > a[0] + a[1] :
    a[2] = a[0] + a[1]
print(a[0] + a[1] + a[2])