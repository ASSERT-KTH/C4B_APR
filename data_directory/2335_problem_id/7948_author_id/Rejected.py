vasya = input()

def removeLetter(vasya, letter):
    number = vasya.find(letter)
    if number >= 0:
        return vasya[number+1:]
    else:
        return ""

temp = vasya
for letter in "hello":
    temp = removeLetter(temp, letter)

if temp == "" and vasya != "hello":
    print("NO")
else:
    print("YES")