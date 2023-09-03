position = [int(i) for i in (input().split())]
position.sort()

print((position[2]-position[1])+(position[1]-position[0]))