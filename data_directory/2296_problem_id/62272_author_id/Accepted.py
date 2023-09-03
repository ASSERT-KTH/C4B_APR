(M, N,) = list(map(int, input().split()))
if M%2==0 and N%2==0:
    print((M*N)//2)
elif (M%2==0 and N%2!=0) or (M%2!=0 and N%2==0):
    print((M*N)//2)
elif M%2!=0 and N%2!=0:
    if M > N:
        print((M*(N-1))//2+(M-1)//2)
    else:
        print((N*(M-1))//2+(N-1)//2)