def solution(word):
    if word.isupper():
        print(word.lower())
    elif str(word[1:]).isupper():
        print(str(word[0]).upper() + str(word[1:]).lower())
    else:
        print(word)
word = input()
solution(word)