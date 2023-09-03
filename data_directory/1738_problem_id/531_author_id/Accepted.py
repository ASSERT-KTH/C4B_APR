'''input
1 1 1
'''
s1, s2, s3 = map(int, input().split())
a, b, c = (s1*s3)//s2, (s1*s2)//s3, (s2*s3)//s1
print(int(4*(a**0.5+b**0.5+c**0.5)))