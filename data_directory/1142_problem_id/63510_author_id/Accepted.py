input_nab = input().split()
n = int(input_nab[0])
a = int(input_nab[1])
b = int(input_nab[2])

# no less than a people standing in front of him
# no more than b people standing behind him

#  >= a people in front
#  <= b people behind

# at least a people in front
# at most b people behind

front = n - a
# 3 1 1 (2)
# 5 2 3 (3)

print(min(front, b+1))