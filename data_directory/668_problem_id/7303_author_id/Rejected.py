x = int(input())
str = ""
for i in range(x,0,-1):
    if i%2==1:
        str += "I hate"
    else:
        str += "I love"
    if i==1:
        str += " it"
    else:
        str += " that "


print(str)