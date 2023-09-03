import math
"""
#include <cstdio>
#include <iostream>
#include <algorithm>

bool isRight(int *c){

    int sides[3] = {0};
    sides[0] = (c[4] - c[2]) * (c[4] - c[2]) + (c[5] - c[3])* (c[5] - c[3]);
    sides[1] = (c[4] - c[0]) * (c[4] - c[0]) + (c[5] - c[1])* (c[5] - c[1]);
    sides[2] = (c[2] - c[0]) * (c[2] - c[0]) + (c[3] - c[1])* (c[3] - c[1]);

    std::sort(sides, sides + 3);
    if(sides[0] > 0 && sides[2] == sides[0] + sides[1]){return 1;}
    else{return 0;}
}


int main(){

    int points[6] = {0};
    for(int k = 0; k < 6; k++){scanf("%d", points + k);}

    std::string output = "NEITHER";
    if(isRight(points)){output = "RIGHT";}
    else{
        for(int k = 0; k < 6; k++){
            ++points[k];    if(isRight(points)){output = "ALMOST"; break;}
            points[k] -= 2; if(isRight(points)){output = "ALMOST"; break;}
            ++points[k];
        }
    }

    std::cout << output << std::endl;
    return 0;
}
"""
def distancia_euclidiana(x, y):
    lados = []
    lados.append(math.pow(x[0] - x[1], 2) + math.pow(y[0] - y[1], 2))
    lados.append(math.pow(x[0] - x[2], 2) + math.pow(y[0] - y[2], 2))
    lados.append(math.pow(x[1] - x[2], 2) + math.pow(y[1] - y[2], 2))
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