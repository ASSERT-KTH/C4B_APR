sand_in, lead_out, lead_in, gold_out, gold_in, sand_out = map(int,
                                                              input().split())
def ron():
    print('Ron')
    import sys; sys.exit()

if lead_out * gold_out * sand_out > sand_in * lead_in * gold_in:
    ron()

if gold_out > 0:
    if lead_in == 0:
        ron()
    if lead_out > 0:
        if sand_in == 0:
            ron()
        if sand_out > 0:
            if gold_in == 0:
                ron()

print('Hermione')