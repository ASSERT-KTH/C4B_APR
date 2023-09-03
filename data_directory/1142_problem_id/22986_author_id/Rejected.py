#position

string = input()
n, a, b = string.split()
a = int(a)
b = int(b)
n = int(n)

front = a
back = b

possible_slots = 0

while b>=0:
	a += 1
	b -= 1
	possible_slots += 1

if front < back:
	possible_slots -= 1

print(possible_slots)