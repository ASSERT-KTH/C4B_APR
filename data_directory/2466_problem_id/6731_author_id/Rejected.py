__author__ = "runekri3"

movements = input()
total_movements = len(movements)
up_count = movements.count("U")
down_count = movements.count("D")
left_count = movements.count("L")
right_count = movements.count("R")

end_x, end_y = 0, 0
end_y += up_count
end_y -= down_count
end_x += right_count
end_x -= left_count

abs_x = abs(end_x)
abs_y = abs(end_y)

if (abs_x == 1 and abs_y == 0) or (abs_x == 0 and abs_y == 1):
    if total_movements > 1:
        print("BUG")
elif abs_x == 0 and abs_y == 0:
    print("BUG")
else:
    last_movement = ""
    for movement in movements:
        if movement == "U" and last_movement == "D":
            print("BUG")
            break
        if movement == "D" and last_movement == "U":
            print("BUG")
            break
        if movement == "L" and last_movement == "R":
            print("BUG")
            break
        if movement == "R" and last_movement == "L":
            print("BUG")
            break
        last_movement = movement
    else:
        print("OK")