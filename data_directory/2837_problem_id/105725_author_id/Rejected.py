def main():
    year = str(int(input())+1)
    originalYear = int(year) - 1
    while (isLucky(year) == False):
        year = str(int(year) + 1)

    print(int(year) - originalYear)

def isLucky(number):
    result = False
    for char in number: 
        if char != '0':
            result = not result
            if result == False:
                return False

    return True
                
main()