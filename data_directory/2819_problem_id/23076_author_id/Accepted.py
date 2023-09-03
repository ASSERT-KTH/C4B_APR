a = input()
l, r = a.split(" ")
#myList = []
#def problem(n):
#    for i in range(1, n+1):
#        if n % i == 0:
#            if(i == 1):
#                continue
#            else:
#                myList.append(i)
#    return myList
#for i in range(int(l), int(r) + 1):
#    problem(i)
#print(max(set(myList), key=myList.count))
if(int(l) == int(r)):
    print(l)
else:
    print("2")