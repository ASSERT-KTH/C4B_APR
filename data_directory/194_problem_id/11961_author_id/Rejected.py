'''input
12
'''

# import sys
# from pprint import pprint
n = int(input())
print(int(n / 5 + 0.5) + (1 if n % 5 else 0))