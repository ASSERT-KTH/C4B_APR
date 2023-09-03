from math import*
n,R,r=map(int,input().split())
if n<3:exit(print(['NO','YES'][n*r<=R+1e-9]))
theta = (pi/180*360/n)
theta2 = ((180-(360/n))/2)
a=2*r+2*r*cos(pi/180*theta2)
b = a*sin((pi-theta)/2)/sin(theta)
print(['NO','YES'][b<=R+1e-9])