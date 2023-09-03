from bisect import bisect_left
arr = [((2*i+1)**2)//2 + 1 for i in range(7)]
n = int(input())
if n == 3:
    print(5)
else:    
    print(2*bisect_left(arr,n)+1)