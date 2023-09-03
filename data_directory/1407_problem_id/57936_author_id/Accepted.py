import math
import re
from fractions import Fraction
from collections import Counter

class Task:
    a, b = 0, 0
    answer = 0
    
    def __init__(self):
        self.a, self.b = [x for x in input().split()]

    def solve(self):
        a, b = self.a, self.b
        self.answer = int(a) + int(b[::-1])

    def printAnswer(self):
        print(self.answer)

task = Task()
task.solve()
task.printAnswer()