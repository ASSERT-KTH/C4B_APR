lista=[]
for i in range(0,4):
    lista.append(input())
contador=0
contador2=0
contador3=0


for j in range(0,len(lista)):
    contador+=lista[j].count('#')
    contador2+=lista[j].count('.')
if contador==contador2:
    for k in range(0,3):
        for j in range(0,3):
       
            if lista[k][j]==lista[k+1][j] and lista[k][j+1]==lista[k+1][j+1] and lista[k][j]==lista[k][j+1]:
                contador3+=1
            elif lista[k][j]==lista[k][j+1] and lista[k+1][j]==lista[k][j] or lista[k][j+1]==lista[k+1][j+1] and lista[k+1][j]==lista[k+1][j+1]:
                contador3+=1
    
    
   
    if contador3>=1:
        print("YES")
    else:
        print("NO")
        
            
    
    
else:
    print("YES")