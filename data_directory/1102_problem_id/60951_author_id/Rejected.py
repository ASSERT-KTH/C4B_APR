w = input().lower()
wf = ''
for itch in range(0, len(w)):
    if (w[itch] == 'a') or (w[itch] == 'e') or (w[itch] == 'i') or (w[itch] == 'o') or (w[itch] == 'u'):
        continue
    else:
        wf += '.' + w[itch]
print(wf)