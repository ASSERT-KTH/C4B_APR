string = input()
vowels = ["A", "E", "I", "O", "U", "Y"]
jumps = []
jump = 1
for x in string:
    if x in vowels:
        jumps.append(jump)
        jump = 1
    else:
        jump += 1
if jumps == []:
    jumps = [len(string) + 1]
print(max(jumps))