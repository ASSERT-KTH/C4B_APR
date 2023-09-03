horseshoes_color = input().split()
count = 0
for i in range(3):
    if horseshoes_color[i] == horseshoes_color[i+1]:
        count = count + 1
    else :
        count = count
        
print(count)