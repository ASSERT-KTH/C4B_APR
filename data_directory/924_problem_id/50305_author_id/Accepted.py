import math

l, d, k = map(int, input().split())


eachLane = 2*d
lane = math.ceil(float(k)/ eachLane)

desk = math.ceil((k % (2*d))/2.0)
if(desk == 0):
	desk = d

if(k%2 == 0):
	print(int(lane), int(desk) , "R")
else:
	print(int(lane), int(desk) , "L")