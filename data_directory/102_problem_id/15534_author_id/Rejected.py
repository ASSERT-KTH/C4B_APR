A=[int(i) for i in input().split()]
B=[A[0]+A[1]+A[2],2*(A[0]+A[1])]
B.sort()
print(B[0])