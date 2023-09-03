def main():
    year = input()
    nextYear = (int(year[0])+1) * 10**(len(year)-1)
    print(nextYear-int(year))            

main()