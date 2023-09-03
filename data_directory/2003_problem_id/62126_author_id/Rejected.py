'''th, hu, do, un = map(str, input())
year = int(th + hu + do + un)'''

year = int(input())

for i in range(year + 1, 9000):
    i = str(i)
    if i[0] != i[1] and i[2] != i[3] and i[1] != i[3] and i[0] != i[2] and i[1] != i[2] and i[0] != i[3]:     
        print(i)
        break