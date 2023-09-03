n = int(input())
print(' '.join(map(str, [i+2 for i in range(n-1)]+[1])))