horseshoes_color = input().split()
count = len(horseshoes_color) - len(list(set(horseshoes_color)))
print(count)