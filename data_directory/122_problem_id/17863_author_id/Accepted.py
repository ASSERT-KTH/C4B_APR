i = input()
j = input()
i = list(i.split(" "))
j = list(j.split(" "))
w = list(input().split(" "))
max = [500,1000,1500,2000,2500]
count = 0
ans = 0
for count in range(5):
	t = float((1 - int(i[count])/250)*int(max[count])-(50*(int(j[count]))))
	ans1 = 0
	ans1 = int(0.3*int(max[count]))
	if ans1 > t:
		ans+=ans1
	else:
		ans+=t
ans+=100 * int(w[0]) - 50 * int(w[1])
print(int(ans))