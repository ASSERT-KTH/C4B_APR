str1=input("")
firststr=str1[0]
secondstr=str1[2]
num=int(input(""))
def switch(x):
    if x=='v' :
        return 1
    if x=='<' :
        return 2
    if x=='^' : 
        return 3
    if x=='>' :
        return 4
i=0
fsn=switch(firststr)
ssn=switch(secondstr)
output="undefined"
outf=0
num=num%4
if num < 1 :
    num+=4
if fsn+num>4 :
    fsnnum=(fsn+num)-4
if fsnnum==ssn :
    output="cw"     
if fsn-num==(4-ssn) or fsn-num==(-4+ssn) :
    output="ccw"
print(output)