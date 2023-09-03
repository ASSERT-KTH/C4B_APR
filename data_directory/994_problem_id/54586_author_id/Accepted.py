from math import ceil

a = input()
b = a.split()
print(ceil(float(b[0]) / float(b[2]))*ceil(float(b[1]) / float(b[2])))