n = int(input())

layers = []

for i in range(n):
    if i % 2 == 0:
        layers.append("hate")
    else:
        layers.append("love")

print("I %s it" % " that I ".join(layers))
# 1496340722803