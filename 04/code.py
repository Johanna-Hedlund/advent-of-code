import numpy as np
import re
with open('/home/johanna/Documents/AdventOfCode/2023/04/data.txt') as f:
    lines = f.readlines()
lines = [l.replace('\n','') for l in lines]
a=[[re.findall(r'[0-9]+',k) for k in l.split(':')[1].split("|")] for l in lines]
winning = [[int(r) for r in a[i][0]] for i in range(len(a))]
draw = [ [int(r) for r in a[i][1]] for i in range(len(a))]

# part 1
numwins=[sum([1 if winning[round].count(num)>0 else 0 for num in draw[round]]) for round in range(len(draw))]
points = [n if n<=1 else 2**(n-1) for n in numwins]
print('part 1: ',sum(points))

# part 2
resultingCardNums=np.ones(len(numwins))
for i,n in enumerate(numwins):
    if n>0:
        resultingCardNums[i+1:i+n+1]+=resultingCardNums[i]
print('part 2: ',sum(resultingCardNums))