a  = int(input())
b = list(map(int,input().split()))
b.sort()
b.reverse()
suma = 0
cont = 0
for i in range(len(b)):
     if(suma>=a):
          break;
     suma += b[i]
     cont += 1
print(cont)