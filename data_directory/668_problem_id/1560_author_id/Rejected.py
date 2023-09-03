a=int(input())

b=a

str=''

while b>0:

	if (a-b)%2==0:

		str+='I hate it '

		b-=1

	else:

		str+='I love it '

		b-=1

print(str)