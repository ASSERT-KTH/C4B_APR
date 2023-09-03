string=(input())
list1=list(string)
x=0
while x <len(list1):
    if((list1[x]=='a' or list1[x]=='e' or list1[x]=='i' or list1[x]=='o' or list1[x]=='u' or list1[x]=='y')):
        list1.pop(x)
        x+=1
    else:
        x+=1
        continue
t=len(list1)
x=0
while x<t:
    list1.insert(2*x,'.')
    x+=1
string=''.join(list1)
print(string)