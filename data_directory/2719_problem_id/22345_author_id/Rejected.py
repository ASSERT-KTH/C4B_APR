def main():
	a = int(input())
	b = int(input())
	count = 0
	
	while a <= b:
		count += 1
		a = a*3
		b = b*2
	
	print(count)
	
if __name__ == '__main__':
	main()