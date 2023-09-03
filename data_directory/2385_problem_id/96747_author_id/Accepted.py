n = int(input())

if -128 <= n <= 127:
	print("byte")
	
else :
	if -32768 <= n <= 32767 :
		
		print("short")
		
	else :
		if -2147483648 <= n <= 2147483647 :
			print("int")
			
		else :
			if -9223372036854775808 <= n <= 9223372036854775807 :
				print("long")
				
			else :
				print("BigInteger")