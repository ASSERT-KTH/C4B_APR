k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

hurt = 0
count = 1

while count <= d:
	if count % k == 0 or count % m == 0 or count % n == 0 or count % l == 0:
		hurt += 1
	count = count + 1	
print (hurt)