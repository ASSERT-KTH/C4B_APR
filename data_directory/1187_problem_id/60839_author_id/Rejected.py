def caps():
    string = input()
    judge = False
    new_string =''
    new_string += string[0].upper()
    if string[0].upper() == string[0]:
        judge = True
    for i in range(1,len(string)):
        if string[i].lower() == string[i]:
            judge = True
        else:
            judge = False
        while judge != False:
            return string
            break
        new_string += string[i].lower()
    return new_string
print(caps())