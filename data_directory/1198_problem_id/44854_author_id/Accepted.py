list = ['H','Q','9']
inputs = input()
def Hqlang(inputs):
    for i in inputs:
        if i in list:
            return "YES"
    return "NO"

print(Hqlang(inputs))