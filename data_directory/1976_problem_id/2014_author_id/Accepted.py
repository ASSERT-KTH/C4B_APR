n=int(input())
x=[ i for i in input()]
the_stack=[x[0]]
del x[0]

while x!=[]:
    if the_stack[-1]==x[0]:
        del x[0]
    else:
        the_stack.append(x[0])
print(n-len(the_stack))