def sex_identifier(user):
    user = set(user)
    if len(user) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM"

print(sex_identifier(input()))