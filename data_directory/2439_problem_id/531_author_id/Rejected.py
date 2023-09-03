'''input
3
-1 -1 2
'''
n = int(input())
a = sorted(map(int, input().split()))
print(sum([abs(x - a[x-1]) for x in range(1,n+1)]))