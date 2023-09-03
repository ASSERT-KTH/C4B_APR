total_pages_nr, min_pages_per_day, max_pages_per_day, delta, reread_pages_nr = (int(x) for x in input().split())
days_nr = 0
pages_read_nr = reread_pages_nr
curr_speed = min_pages_per_day
while pages_read_nr < total_pages_nr:
    pages_read_nr -= reread_pages_nr
    pages_read_nr += curr_speed
    curr_speed += delta
    if curr_speed > max_pages_per_day:
        curr_speed = max_pages_per_day
    days_nr += 1
    
print(days_nr)