n = int(input())
i = 0

while 5*(2**i) < n:
    i += 1

rest = n - 5*(2**(i-1))

if i == 0:
    if n == 1:
        print("Sheldon")
    elif n == 2:
        print("Leonard")
    elif n == 3:
        print("Penny")
    elif n == 4:
        print("Rajesh")
    else:
        print("Howard")
elif rest / (5*(2**(i))) <= 0.2:
    print("Sheldon")
elif rest / (5*(2**(i))) <= 0.4:
    print("Leonard")
elif rest / (5*(2**(i))) <= 0.6:
    print("Penny")
elif rest / (5*(2**(i))) <= 0.8:
    print("Rajesh")
else:
    print("Howard")