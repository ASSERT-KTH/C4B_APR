x=input()

def limites():
    pos = 8
    if x1[1] == "1" or  x1[1] == "8":
        pos -= 3
    if x[0] == "a" or x[0] == "h":
        pos -= 3
    if pos == 2:
        pos += 1
    return pos
print(limites())