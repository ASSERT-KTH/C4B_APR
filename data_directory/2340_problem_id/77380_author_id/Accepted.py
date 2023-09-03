def main():
    from string import ascii_uppercase as upp
    s=input()
    q=0
    q1=0
    for i in s:
        if i in upp:
            q+=1
        else:
            q1+=1
    if q<=q1:
        print(s.lower())
    else:
        print(s.upper())
main()