size=input()
inp=input()

counter=0
separator_zero=True
number=''
for l in inp:
    if l != '0':
        separator_zero=True
        counter+=1

    else:
        if counter>0:
            number+=str(counter)
            separator_zero=False
            counter=0
        else:
            if separator_zero:
                separator_zero=False
            else:
                number+='0'
                separator_zero=True

number+=str(counter)

print(number)