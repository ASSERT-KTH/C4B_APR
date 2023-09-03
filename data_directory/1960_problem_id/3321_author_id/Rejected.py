F1 = str(input())
F2 = str(input())
F3 = str(input())
F4 = str(input())
F5 = str(input())

if F1[0]=="1" or F5[0]=="1" or F1[8]=="1" or F5[8]=="1":
    print (4)
elif F1[2]=="1" or F1[6]=="1" or F2[0]=="1" or F2[8]=="1" or F4[0]=="1" or F4[8]=="1" or F5[2]=="1" or F5[6]=="1":
    print (3)
elif F1[4]=="1" or F2[2]=="1"or F2[6]=="1" or F4[2]=="1" or F4[6]=="1" or F3[0]==1 or F3[8]=="1" or F5[4]=="1":
    print (2)
elif F2[4]=="1" or F3[2]=="1" or F3[6]=="1" or F4[4]=="1":
    print (1)
else: print (0)
# 1502656328119