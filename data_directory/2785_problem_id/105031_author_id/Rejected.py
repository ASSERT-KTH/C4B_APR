'''
    Вредная Клавиатура
    http://codeforces.com/problemset/problem/801/A

    У Тонио есть клавиатура с двумя клавишами: буквой «V» и буквой «K».

    Однажды он набрал строку s, используя только эти две буквы. Ему нравится, когда он
    встречает подстроку «VK», поэтому он хочет изменить не больше одной буквы в строке
    (или не изменять ничего), чтобы максимизировать число вхождений этой подстроки.
    Вычислите максимальное число раз, которое строка «VK» может встретиться как
    подстрока (т. е. буква «K» сразу после буквы «V») в получившейся строке.

    Входные данные
    Единственная строка содержит строку s, которая состоит только из заглавных букв
    латинского алфавита «V» или «K» и имеет длину от 1 до 100.

    Выходные данные
    Выведите одно число — максимальное число раз, которое строка «VK» может встречаться
    как подстрока в данной строке после изменения не более одного символа.
'''

import fileinput



def get_max_vk(input_string):

    if not isinstance(input_string, str):
        raise TypeError('Value should be string')

    s_len = len(input_string)

    if s_len < 1 or s_len > 100:
        raise ValueError('String length should be between 1 and 100')

    last_char = ''
    total = 0
    can_sub = False

    for char in input_string:

        if char == 'V':

            if last_char == 'V':
                can_sub = True

        elif char == 'K':

            if last_char == 'V':
                total += 1

            elif last_char == 'K':
                can_sub = True

        else:
            raise ValueError('Input contains invalid character: ' + char)

        last_char = char

    return total + (1 if can_sub else 0)



if __name__ == '__main__':

    for line in fileinput.input():
        print(get_max_vk(line.rstrip("\n")))