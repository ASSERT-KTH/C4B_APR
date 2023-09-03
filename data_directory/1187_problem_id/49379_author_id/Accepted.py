ls = input()
def m_str(lsr):
    ls2 = []
    for k in ls:
        if str.islower(k):
            ls2.append(str.upper(k))
        elif str.isupper(k):
            ls2.append(str.lower(k))
    return ls2
if len(ls) == 1:
    if str.isupper(ls):
        print(str.lower(ls))
    elif str.islower(ls):
        print(str.upper(ls))
elif (str.isupper(ls)) | (str.isupper(ls[1:]) & (str.isupper(ls[0]) == False)):
    lsk = m_str(ls)
    for k in lsk:
        print(k, end='')
else:
    print(ls)