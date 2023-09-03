*m,d=(int(input()) for i in range(5))
print(sum(any((i+1)%k for k in m) for i in range(d)))