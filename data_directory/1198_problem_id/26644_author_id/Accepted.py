word = input()

print("YES" if word.find(chr(72)) > -1 or word.find(chr(81)) > -1 or word.find(chr(57)) > -1 else "NO")