m=input().split()
w=input().split()
h=input().split()
s=0
for i in range(5):
  s=s+max(0.3*500*(i+1),(1-int(m[i])/250)*500*(i+1)-50*int(w[i]))
s=s+int(h[0])*100-int(h[1])*50
print(int(s))