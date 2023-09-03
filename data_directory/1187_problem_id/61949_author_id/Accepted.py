def render(input):
    if (input[1:].upper() == input[1:]):
        return input.swapcase()
    return input

print(render(input()))