string = input("")
chars = "abcdefghijklmnopqrstuvwxyz"
total = len(string)
for char in chars:
  count = string.count(char)
  if count > 1:
      total -= (count-1)
if(total % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")