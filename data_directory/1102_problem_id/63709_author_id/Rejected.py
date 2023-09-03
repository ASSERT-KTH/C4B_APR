word = input()
list=[]
for letter in word:
  if letter not in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U' ):    
    list.append(letter)    
for i in range(len(list)):
  print('.', end='') 
  print(list[i].lower(), end='') ,