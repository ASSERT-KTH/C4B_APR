a=int(input())

i=0

while 5*(2**i-1)<a:

    i+=1


if 5*(2**(i)-1)-5*2**(i-1)+1 <= a < 5*(2**(i)-1)-4*2**(i-1)+1:

    print("Sheldon")



elif 5*(2**(i)-1)-4*2**(i-1)+1 <= a < 5*(2**(i)-1)-3*2**(i-1)+1:

    print("Leonard")



elif 5*(2**(i)-1)-3*2**(i-1)+1 <= a < 5*(2**(i)-1)-2*2**(i-1)+1:

    print("Penny")



elif 5*(2**(i)-1)-2*2**(i-1)+1 <= a < 5*(2**(i)-1)-1*2**(i-1)+1:

    print("Rajesh")



elif 5*(2**(i)-1)-2**(i-1)+1 <= a < 5*(2**(i)-1)+1:

    print("Howard")