a=int(input())
x=''
while a:
    if a%2:x='that I hate '+x
    else:x='that I love '+x
    a-=1
print(x[5:]+'it')