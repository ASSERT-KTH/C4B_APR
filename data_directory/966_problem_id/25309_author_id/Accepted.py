hobbits_nr, pillows_nr, frodos_place = (int(x) for x in input().split())

pillows_nr = pillows_nr - hobbits_nr
frodos_pillows = 1

# [left, right) -- it's a half-interval
left = frodos_place
right = frodos_place + 1

while pillows_nr >= right - left:
    pillows_nr -= right - left
    frodos_pillows += 1
    right += 1
    left += -1
    if right > hobbits_nr + 1:
        right = hobbits_nr + 1
    if left < 1:
        left = 1
    if left == 1 and right == hobbits_nr + 1:
        frodos_pillows += pillows_nr // hobbits_nr
        pillows_nr = pillows_nr % hobbits_nr
# print(pillows_nr)
# print(left, right)
print(frodos_pillows)