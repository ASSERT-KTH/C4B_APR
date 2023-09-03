def main():
	string = input().strip()
	
	for letter in string:
		if letter in ['H', 'Q', '9']:
			print('YES')
			return(0)
	print('NO')
	return(0)

if __name__ == '__main__':
	main()