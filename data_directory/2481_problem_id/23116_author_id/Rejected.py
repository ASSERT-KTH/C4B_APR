# http://codeforces.com/problemset/problem/82/A

n = int(input())

li = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


# s1 l2 p3 r4 h5 
# s6 s7 l8 l9 p10 p11 r12 r13 h14 h15
# s16 s17 s18 s19 l20 l21 l22 l23 p24 p25 p26 p27 r28 r29 r30 r31 h32 h33 h34 h35 

if n<=5:
  print(li[n-1])
else:
  nn = n-5
  for i in [5, 4, 3, 2, 1]:
    if nn%i==0:
      print(li[i-1])
      break