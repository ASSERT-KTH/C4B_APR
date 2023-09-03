l = ['Sheldon','Leonard','Penny','Rajesh','Howard']
n = int(input().strip())
i = 1
while i * 5 < n: n -= i * 5; i *= 2
print(l[(n-1)//i])