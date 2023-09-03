s = str(input())
a = s.count("VK")
s = s.replace("VK", "TP")
if (s.find("VV")!=-1 or s.find("KK")!=-1):
    a += 1
print (a)