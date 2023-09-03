month, first_day = (int(x) for x in input().split())

month_to_len = {1: 31, 2: 28,
                3: 31, 4: 30,
                5: 31, 6: 30,
                7: 31, 8: 31,
                9: 30, 10: 31,
                11: 30, 12: 31
               }
               
len_to_start = {28: 1, 
                30: 6, 
                31: 5
               }
               
len_to_min_columns = {28: 4,
                      30: 5,
                      31: 5
                     }

month_len = month_to_len[month]
columns_nr = len_to_min_columns[month_len]
if first_day > len_to_start[month_len]:
    columns_nr += 1
    print(columns_nr)
else:
    print(columns_nr)