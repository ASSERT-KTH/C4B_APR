name_user = str(input())
list_name_user=[]
for item in name_user:
  list_name_user.append(item)
n=len(list_name_user)
# print (list_name_user)
for i in range (n):
  j=i+1
  while j < n:
    if list_name_user[i]==list_name_user[j]:
      del list_name_user[j]
      n-=1
      print (list_name_user)
    else:
      j+=1
if n%2!= 0:
  print('IGNORE HIM!')
else:
  print('CHAT WITH HER!')