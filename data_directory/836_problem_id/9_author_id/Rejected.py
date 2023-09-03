players = int(input())

games = 0

while True:
  lastpcount = players
  players = players//2
  games += 1
  if 2 * players == lastpcount and players == 1:
    break
  elif 2 * players != lastpcount:
    players += 1
    
print(games)