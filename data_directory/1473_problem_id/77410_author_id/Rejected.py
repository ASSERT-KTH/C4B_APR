import math

def distancia_euclidiana(x, y):
    lados = []
    lados.append(math.sqrt(math.pow(x[0] - x[1], 2) + math.pow(y[0] - y[1], 2)))
    lados.append(math.sqrt(math.pow(x[0] - x[2], 2) + math.pow(y[0] - y[2], 2)))
    lados.append(math.sqrt(math.pow(x[1] - x[2], 2) + math.pow(y[1] - y[2], 2)))
    return sorted(lados)


def is_right(pontos):
    distancias = distancia_euclidiana((pontos[0], pontos[2], pontos[4]), (pontos[1], pontos[3], pontos[5]))
    #return math.pow(distancias[2], 2) == math.pow(distancias[0], 2) + math.pow(distancias[1], 2)
    return distancias[0] > 0 and distancias[2] == distancias[1] + distancias[0]


pontos = [int(i) for i in input().split()]

resultado = 'NEITHER'

if is_right(pontos):
    resultado = 'RIGHT'
else:
    for i in range(0, 6):
        pontos[i] += 1
        if is_right(pontos):
            resultado = 'ALMOST'
            break
        pontos[i] -= 2
        if is_right(pontos):
            resultado = 'ALMOST'
            break
        pontos[i] += 1

print(resultado)