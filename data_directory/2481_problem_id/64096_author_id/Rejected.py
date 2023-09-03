count = int(input())
data = {0: "Sheldon", 1: "Leonard", 2: "Penny", 3: "Rajesh", 4: "Howard"}
j = 0
k = 0
while count > 0:
    count -= 2 ** j
    if count - 2**j < 0:
        print(data[k])
        break
    k += 1
    if(k == 4):
        j += 1
        k = 0