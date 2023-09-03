k = int(input())

r = 0

for i in range(k-1):
    r += (k - i)*(i + 1) - i
        
print(r+1)