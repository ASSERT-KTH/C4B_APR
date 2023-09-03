#problem 825A
size=int(input())
string=input()
answer=[]
list_=list(string)
#print(list_)
memory=1
counter=0
for i in range(0,size):
    #print(i," ",list_[i])
    if int(list_[i])==memory:
        #print("Checkpoint 1")
        counter+=memory
    else:
        #print("Checkpoint 2")
        answer.append(counter)
        counter=0
        if memory==1:
            memory=0
            counter+=memory
        else:
            memory=1
            counter+=memory
answer.append(counter)
mystring = ""
for digit in answer:
    mystring += str(digit)
print(mystring)