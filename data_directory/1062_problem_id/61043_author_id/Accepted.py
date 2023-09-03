luckyNums = [4, 7]
lucky = 0

for i in str(input()):
    lucky += int(i) in luckyNums

print("YES" if lucky in luckyNums else "NO")