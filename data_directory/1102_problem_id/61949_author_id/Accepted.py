def render(input):
	ret = input.lower()
	for vowel in "aeiouy":
		ret = ret.replace(vowel, '')
	ret = map((lambda c: '.' + c), ret)
	return ''.join(ret)

def main():
	print(render(input()))


main()