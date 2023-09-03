n = int(input())
i = 0

while 5*(2**i) < n:
    n = n - 5*(2**i)
    i += 1



if n / (5*(2**(i))) <= 0.2:
    print("Sheldon")
elif n / (5*(2**(i))) <= 0.4:
    print("Leonard")
elif n / (5*(2**(i))) <= 0.6:
    print("Penny")
elif n / (5*(2**(i))) <= 0.8:
    print("Rajesh")
else:
    print("Howard")