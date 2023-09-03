import math
n = int(input())
x=input()
day=x.split(" ")
day_pages=[]
for i in range(7):
    day_pages.append(int(day[i]))
sum1=0
while True:
    for i in range(0,6):
        sum1+=day_pages[i]
        if sum1 >n or sum1 == n:
            print(i+1)
            exit()