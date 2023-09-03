'''input
1 1 5
'''
d1, d2, d3 = map(int, input().split())
print(min(2*d1+2*d2, d1+d2+d3))