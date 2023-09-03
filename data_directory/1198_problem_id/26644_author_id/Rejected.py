word = input()

print("YES" if word.find(chr(72)) > -1 or word.find(chr(81)) > -1 or word.find("+") > -1 or word.find("9") > -1 else "NO")