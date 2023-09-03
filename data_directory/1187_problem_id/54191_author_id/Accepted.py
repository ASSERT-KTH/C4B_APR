input_str = input()

first_case = True
second_case = True

if input_str[0].isupper():
    second_case = False
else:
    first_case = False

for letter in input_str[1:]:
    if letter.islower():
        first_case = False
        second_case = False

if first_case:
    print(input_str.lower())
elif second_case:
    print(input_str.capitalize())
else:
    print(input_str)