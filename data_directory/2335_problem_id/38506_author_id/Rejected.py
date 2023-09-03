input_word = input()
exists = True

for i, c in enumerate("hello"):
    print(input_word)
    if input_word.find(c) >= 0:
        input_word = input_word[input_word.index(c) + 1:]
    else:
        exists = False
        break

print(exists and "YES" or "NO")