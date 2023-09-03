n = int(input())

print(' '.join(map(str, [n]+[i+1 for i in range(n-1)])))