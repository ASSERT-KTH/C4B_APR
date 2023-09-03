number = str(input())

fours = number.count("4")
sevens = number.count("7")

lucky = fours + sevens

print("YES" if lucky > 3 and (lucky % 7 == 0 or lucky % 4 == 0) else "NO")