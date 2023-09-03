def check_tri(Line):
    for i in range(2):
        for j in range(i+2, 4):
            if Line[i+1] + Line[i] > Line[j] and Line[i] + Line[j] > Line[i+1] and Line[i+1] + Line[j] > Line[i]:
                return True
    return False
    
def check_ln(Ln):
    Con1 = Ln[0] + Ln[1] == Ln[2] or Ln[1] + Ln[2] == Ln[3] or Ln[2] + Ln[3] == Ln[0]
    Con2 = Ln[0] + Ln[1] == Ln[3] or Ln[1] + Ln[2] == Ln [0] or Ln[2] + Ln[3] == Ln[1]
    Con3 = Ln[0] + Ln[2] == Ln[1] or Ln[1] + Ln[3] == Ln[2] or Ln[3] + Ln[0] == Ln[2]
    Con4 = Ln[0] + Ln[2] == Ln[3] or Ln[1] + Ln[3] == Ln [0] or Ln[3] + Ln[0] == Ln[1]
    if Con1 or Con2 or Con3 or Con4:
        return True
    else:
        return False
        
    
def main():
    Line = input()
    Line = Line.split()
    if type(Line) != list:
        print('Enter 4 numbers separated by spaces!')
        main()
    for i in range(len(Line)):
        Line[i] = eval(Line[i])
    for i in Line:
        if len(Line) != 4 or type(i) != int or i <= 0 or i > 100:
            print('Enter exactly 4 positive integers lesser than 100!')
            main()
    if check_tri(Line):
        print('TRIANGLE')
    elif check_ln(Line):
        print('SEGMENT')
    else:
        print('IMPOSSIBLE')


main()