nk = input().split(" ")
n,k = [int(x) for x in nk]
k -= 1
gen_list = [1]
for i in range(1,n):
    j = i+1
    aux = gen_list.copy()
    gen_list.append(j)
    gen_list.extend(aux)
print(gen_list[k])