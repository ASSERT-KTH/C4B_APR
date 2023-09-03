def main():
	nums = list(map(int, input().split()))
	a = nums[0] * nums[1] + nums[3] * 2
	b = nums[0] * nums[2] + nums[4] * 2

	if a < b:
		print("First")
	elif a == b:
		print("Friendsship")
	else:
		print("Second")

if __name__ == '__main__':
	main()