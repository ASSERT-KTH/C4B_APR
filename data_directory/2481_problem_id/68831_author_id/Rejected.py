import math
n = int(input())
l = int(math.log2((n-1)/5+1))
dict = {1:'Sheldon',2:'Leonard',3:'Penny',4:'Rajesh',5:'Howard'}
m = n - 5*(2**l-1)
m = m//(2**l-1)+1
print(dict[m])