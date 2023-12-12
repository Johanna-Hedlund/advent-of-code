import numpy as np
import re
with open('./data.txt') as f:
    lines = f.readlines()
# replace newlines
lines = [re.sub(r'Game\s[0-9]*:', '',l) for l in lines]
lines = [re.sub(r'\n', '',l) for l in lines]

draw_matrix = [[draw for draw in l.split(';')] for l in lines]

matrix_red = [[int((re.findall('[0-9]*.(?=red)',l) or [0])[0]) for l in m] for m in draw_matrix]
matrix_blue = [[int((re.findall('[0-9]*.(?=blue)',l) or [0])[0]) for l in m] for m in draw_matrix]
matrix_green = [[int((re.findall('[0-9]*.(?=green)',l) or [0])[0]) for l in m] for m in draw_matrix]

max_red_blue_green=[[max(r),max(b),max(g)] for r,b,g in zip(matrix_red,matrix_blue,matrix_green)]
isWithinLimit=[all([max(r)<=12,max(b)<=14,max(g)<=13]) for r,b,g in zip(matrix_red,matrix_blue,matrix_green)]

#part1
print('part 1: ',sum( [i+1 if  max_red_blue_green[i] else 0 for i in range(len(max_red_blue_green))]))

#part 2
power=[m*g*b for m,g,b in max_red_blue_green]
print('ppart 2: ',sum(power))
