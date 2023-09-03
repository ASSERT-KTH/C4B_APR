a =input()


if(1<=len(a)<=100):


      if("H" in a):
          print("YES")

      if ("Q" in a):
          print("YES")

      if ("(" in a):
          print("YES")

      else:
          print("NO")



else:
    print("too long string")