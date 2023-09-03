'''input
0
'''
n = int(input())
print([8, 4, 2, 6][(n % 4 - 1)] if n != 0 else 1)