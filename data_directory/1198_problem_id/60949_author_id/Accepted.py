word = input()
instruction = False
for i in range(len(word)):
    if(word[i]=="H")or(word[i]=="Q")or(word[i]=="9"):
        instruction = True
        break
if(instruction):
    print("YES")
else:
    print("NO")