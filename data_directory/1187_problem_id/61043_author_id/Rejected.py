word = str(input())
print(word[0].upper() + word[1:].lower() if word.upper() == word or word[1:].upper() == word[1:] else word)