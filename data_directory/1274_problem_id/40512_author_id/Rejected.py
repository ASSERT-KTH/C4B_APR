k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
wynik = 0
for i in range (0,d):
    if i%k==0 or i%l==0 or i%m==0 or i%n==0:
        wynik += 1
print(wynik)