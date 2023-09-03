# coding: utf-8
import sys

__author__ = 'buyvich'

SUCCESS_HACK = 100
UNSUCCESS_HACK = 50
MAX_SCORES = 20000

def get_win_places(scores):
    res = []
    k = (scores//50)%475
    for _ in range(25):
        k = (k * 96 + 42)%475
        res.append(26 + k)
    return res

def find_success_hack_count(place, current_scores, goal):
    """
    >>> find_success_hack_count(239, 10880, 9889)
    0
    >>> find_success_hack_count(26, 7258, 6123)
    2
    >>> find_success_hack_count(493, 8000, 8000)
    24
    >>> find_success_hack_count(101, 6800, 6500)
    0
    >>> find_success_hack_count(329, 19913, 19900)
    8
    """
    if place in get_win_places(int(current_scores)):
        return 0
    else:
        i = goal
        negative_diff = 0
        while i <= current_scores:
            win_places = get_win_places(i)
            if place in win_places and not (current_scores-i)%UNSUCCESS_HACK:
                negative_diff = current_scores - i
            i += 50
        j = current_scores
        positive_diff = MAX_SCORES
        cont = True
        while cont:
            win_places = get_win_places(j)
            diff = j-current_scores
            if place in win_places and not diff%UNSUCCESS_HACK:
                positive_diff = diff
                cont = False
            j += 50
        if negative_diff > 0:
            return 0
        else:
            return round(positive_diff/SUCCESS_HACK)


if __name__ == '__main__':
    place, current_scores, goal = sys.stdin.readline().strip().split(' ')
    success_hacks_count = find_success_hack_count(int(place),
                                                  int(current_scores),
                                                  int(goal))
    sys.stdout.write('%s' % success_hacks_count)


# vim:ts=4:sts=4:sw=4:tw=85:et: