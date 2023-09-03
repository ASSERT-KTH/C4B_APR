entrada=input().split(" ")
listae = list(map(int, entrada))#Convertir strs a int
stock=1
while(listae[0]*stock+listae[1]<=listae[3] and listae[2]>0):
    stock=listae[0]*stock+listae[1]
    listae[2]-=1
print(listae[2])