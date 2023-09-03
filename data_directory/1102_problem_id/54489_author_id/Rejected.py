word = ""
arr_1 = ["A", "O", "Y", "E", "U", "I"]
arr_2 = ["a", "o", "y", "e", "u", "i"]
arr_3 =[]
string = input()
arr = []
arr_final = []
count = 0
for i in string:
    arr.append(i)
print(arr)
for i in arr:
    if i not in arr_1 and i not in arr_2:
        arr_final.append(i.lower())
print("." + ".".join(arr_final))