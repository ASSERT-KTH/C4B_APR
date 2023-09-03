players = input()
zero_output = ""
one_output = ""
count = 0
for x in players:
    count += 1
    if x == "0" :
        one_output = ""
        zero_output = zero_output + x
        if len(zero_output) == 7:
            print ("YES")
            break
        elif count == len(players):
            if len(one_output) < 7 or len(zero_output)<7:
                print ("NO")
                break
    elif  x == "1" :
        zero_output = ""
        one_output = zero_output + x
        if len(one_output) == 7:
            print ("YES")
            break
        elif count == len(players):
            if len(one_output) < 7 or len(zero_output)<7:
                print ("NO")
                break