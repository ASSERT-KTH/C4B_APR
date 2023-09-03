entrada = str(input())
entrada = entrada.lower()

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

saida = "."

for letra in entrada:
  
  if letra not in vogais:
   
    saida += letra + "."
 
saida = saida[:-1]

print(saida)