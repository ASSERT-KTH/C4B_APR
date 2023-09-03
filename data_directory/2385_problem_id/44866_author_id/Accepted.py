integer = int(input())
types = (('byte', 7), ('short', 15), ('int', 31), ('long', 63), ('BigInteger', 100000))
print([type_ for type_, val in types if 2 ** val > integer][0])