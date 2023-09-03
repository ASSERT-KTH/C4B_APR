players = int(input())

if players == 2:
  print(1)
elif players == 3:
  print(2)
  
else:
  fib = 3
  fist = 2
  sec = 3
  answer = 2
  
  while fib < players:
    answer += 1
  
    fib = fist + sec
    fist = sec
    sec = fib
  
  if fib > players:
    answer -= 1
    
  print(answer)