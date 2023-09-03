sides = [int(i) for i in input().split()]
#sides = [3 ,5 ,9 ,1]

a, b, c, d = sides
#   print(a, b, c, d)
if a + b > c and a + c > b and c + b > a:
    print("TRIANGLE")
elif a + c > d and a + d > c and c + d > a:
    print("TRIANGLE")
elif b + c > d and b + d > c and c + d > b:
    print("TRIANGLE")
elif a + d > b and a + b > d and b + d > a:
    print("TRIANGLE")
elif a + b == c or a + c == b or c + b == a:
    print("SEGMENT")
elif a + c == d or a + d == c or c + d == a:
    print("SEGMENT")
elif b + c == d or b + d == c or c + d == b:
    print("SEGMENT")
elif a + d == b or a + b == d or b + d == a:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")


# if __name__ == "__main__":
#     print(build_triangle(sides))