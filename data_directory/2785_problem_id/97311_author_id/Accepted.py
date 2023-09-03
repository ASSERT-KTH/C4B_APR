s=input()
c=s.count("VK")
s=s.replace("VK","ms")
if "VV" in s or "KK" in s:
    c+=1
print(c)