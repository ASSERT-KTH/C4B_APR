def main():
	a = [eval(i) for i in input().split()]
	a.sort()
	if(a[1]+a[2]>a[3] or a[0]+a[1]>a[2]): print("TRIANGLE")
	elif(a[0]+a[1]==a[2] or a[0]+a[1]==a[3] or a[1]+a[2]==a[3]): print("SEGMENT")
	else: print("IMPOSSIBLE")

	
main()