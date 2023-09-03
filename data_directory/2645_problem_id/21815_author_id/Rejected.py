plus = int(input())
start = int(input())
start = (plus + (3 - start))%6
if start <= 1:
    print("2")
elif start == 2 or start == 5:
    print("1")
else:
    print("0")