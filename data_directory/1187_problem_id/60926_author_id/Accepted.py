lisa= input()
if(lisa==lisa.upper()):
    print(lisa.lower())
elif(lisa==(lisa[0].lower()+lisa[1:].upper()) and len(lisa)>1):
    print(lisa[0].upper()+lisa[1:].lower())
elif(len(lisa)==1):
    print(lisa.upper())
else:
    print(lisa)