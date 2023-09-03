def main():
	a = [eval(input()), eval(input()), eval(input()), eval(input())]
	a.sort()
	if(a[1]+a[2]>a[3] or a[0]+a[1]>a[2]): print("TRIANGLE")
	elif(a[0]+a[1]==a[2] or a[0]+a[1]==a[3] or a[1]+a[2]==a[3]): print("SEGMENT")
	else: print("IMPOSSIBLE")

	
main()