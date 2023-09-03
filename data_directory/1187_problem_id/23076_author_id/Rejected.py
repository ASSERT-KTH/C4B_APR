string = input()
alpha = ("abcdefghijklmnopqrstuvwxyz")
firstletter = string[0]
if((firstletter in alpha and string[1:] == string[1:].upper())):
    string = string.capitalize()
    print(string)
elif(string == string.upper() ):
    print(string.lower())