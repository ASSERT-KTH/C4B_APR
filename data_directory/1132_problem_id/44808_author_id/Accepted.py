lukcyNumbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

givenNumber = int(input())

for number in lukcyNumbers:
    if givenNumber % number == 0:
        print("YES")
        exit()
    
print("NO")