vasya = input()

def removeLetter(name, letter):
    number = name.find(letter)
    if number >= 0:
        return name[number+1:]
    else:
        return "."

temp = vasya
for letter in "hello":
    temp = removeLetter(temp, letter)

if temp == "." and vasya != "hello":
    print("NO")
else:
    print("YES")