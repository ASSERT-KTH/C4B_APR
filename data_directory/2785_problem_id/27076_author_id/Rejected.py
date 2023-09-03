s=input()
ans=s.count("VK")
s=s.replace("VK","--")
print(s)
if s.find("VV")>-1 or s.find("KK")>-1: ans+=1
print(ans)