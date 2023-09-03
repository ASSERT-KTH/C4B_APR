number = int(input())
n = int((1+(1+8*(number-1))**(1/2))/2)
print(number - n*(n-1)//2)