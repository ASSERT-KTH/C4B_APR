s = input()
flag = 0

if(s.isupper() == "True"):
    for letter in s:
        if flag==0:
            print(letter.upper(),end="")
            flag=1
        else:
            print(letter.lower(),end="")
else:
    if(len(s)<=1):
        print(s.upper(),end="")
    elif(len(s)>1):
        if((s[0].isupper()== 1) and (s[1].islower() == 1)):
            print(s)
        else:
            for letter in s:
                if flag==0:
                    print(letter.upper(),end="")
                    flag=1
                else:
                    print(letter.lower(),end="")