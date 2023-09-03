def ginp():
	return map(int, input().split())
	
n = int(input())
x = int(input())
n = n%5

m = [[0, 1, 2], 
[1, 0, 2], 
[1, 2, 0], 
[2, 1, 0], 
[2, 0, 1], 
[0, 2, 1]]

print(m[n][x])