#You are given a rectangular board of M × N squares. Also you are given an unlimited number of standard domino pieces of 2 × 1 squares. 
#You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:
#1. Each domino completely covers two squares.
#2. No two dominoes overlap.
#3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.
#Find the maximum number of dominoes, which can be placed under these restrictions.
import math
dimension = input()
dim = dimension.split()
M = math.floor(int(dim[0]))
N = math.floor(int(dim[1]))
#domino = 2x1 squares
if M%2 == 1:
    print (int((((M-1)/2)*N)+(N/2)))
else:
    print (int((M/2)*N))