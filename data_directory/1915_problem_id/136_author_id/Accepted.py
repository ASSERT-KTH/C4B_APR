n=int(input())
a=[int(i) for i in input().split()]
b=3*[0]
d=['chest','biceps','back']
for i in range(n):
    b[i%3]+=a[i]
z=b.index(max(b))
print(d[z])