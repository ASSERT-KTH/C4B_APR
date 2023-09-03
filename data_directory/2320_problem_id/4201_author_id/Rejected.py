import itertools

terms = list(map(int, input().split()))
operators = input().split()

def seek(terms, operators):
	best = None
	if len(terms) == 1:
		return terms[0]
	for i, a in enumerate(terms):
		for  j in range(i + 1, len(terms)):
			b = terms[j]
			for k, operator in enumerate(operators):
				if operator == '+':
					x = a + b
				else:
					x = a * b
				y = seek(terms[:i] + terms[i + 1:j] + terms[j + 1:] + [ x ],
						operators[:k] + operators[k + 1:])
				if best == None or y < best:
					best = y
	return best

print(seek(terms, operators))