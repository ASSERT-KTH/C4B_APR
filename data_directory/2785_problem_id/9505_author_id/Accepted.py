string=input()

ans=string.count("VK")

string=string.replace("VK"," ")

ans+=1 if "VV" in string or "KK" in string else 0

print(ans)