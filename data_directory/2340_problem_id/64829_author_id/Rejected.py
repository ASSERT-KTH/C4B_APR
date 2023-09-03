#Word problem in codeforces.com

word = input()
count_upper = sum(map(str.isupper, word))
count_lower = sum(map(str.islower, word))

if count_upper >= count_lower:
    print(word.upper())
else:
    print(word.lower())