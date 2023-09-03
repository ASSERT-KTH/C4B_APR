"Receiving word inputs"
word = input("")

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"

counter = 0
First_letter = word[0]
Rest = word[1:len(word)]

for letter in Rest:
    if letter in upper_case:
        counter += 1
        
if counter == len(Rest):
    " Whether or not the first letter is upper or lower case letter,"
    "If the remaining letters are all uppercase, then Caps lock has been deployed accidentally"
    New_word = First_letter.upper()
    for letter in Rest:
        New_word += letter.lower()

    print(New_word)
else:
    " The rest of the letter is a combination of upper and lower case letter"
    print(word)