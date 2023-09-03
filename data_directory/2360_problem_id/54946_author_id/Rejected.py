gl, gr = [int(i) for i in input().split()]
bl, br = [int(i) for i in input().split()]

if ((gl * 2 + 2) >= br and (abs(gl - br) <= 1)) or ((gr * 2 + 2) >= bl and (abs(gr - bl) <= 1)):
    print("YES")
else:
    print("NO")