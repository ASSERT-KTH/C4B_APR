def render(input):
    if (input[1:].upper() == input[1:]):
        return input[:1].upper() + input[1:].lower()
    return input

print(render(input()))