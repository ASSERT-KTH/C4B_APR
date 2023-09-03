def main():
    string=input().lower()
    list=['a','e','i','o','u','y']
    for x in list:
        temp=string.replace(x,'')
        string=temp
    print('.'+'.'.join(string))



if __name__=='__main__':
    main()