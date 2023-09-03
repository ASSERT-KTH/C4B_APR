n, a,b,c = map(int, input().split())
print( max((i//a + j // b + (n - i - j) // c) for i in range(0,n+1,a) for j in range(0,n+1,b) if (n-i-j) % c == 0))