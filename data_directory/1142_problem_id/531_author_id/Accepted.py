'''input
9 4 3
'''
n, a, b = map(int, input().split())
print(min(n-a,b+1))