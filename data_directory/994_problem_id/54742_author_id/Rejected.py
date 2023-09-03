n=int(input());
m=int(input());
a=int(input());
 
h = n//a;
if n%a != 0: h+=1;
 
w = m//a;
if m%a != 0: w+=1;
 
print(h*w);