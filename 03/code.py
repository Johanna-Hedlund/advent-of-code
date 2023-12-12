import numpy as np
import re

with open('./data.txt') as f:
    lines = f.readlines()
lines = [l.replace('\n','') for l in lines]
matrix_is_symbol = np.array([[True if len(re.findall(r'[^0-9,\.]{1}',l))>0 else False for l in m] for m in [*lines]])
matrix_is_symbol=np.pad(matrix_is_symbol,1)
# is there a symbol in neighborhood?
matrix_is_symbol_neighborhood =np.array([[any(matrix_is_symbol[l-1:l+2,m-1:m+2].flatten()) for m in range(1,141) ] for l in range(1,141) ])

results=[]
for n,line in enumerate(lines):
    p    = re.compile("[0-9]+")
    for m in p.finditer(line):
             results.append([n,m.start(),m.end(),m.group()])

sum=sum([int(results[int(i)][3]) if any(matrix_is_symbol_neighborhood[results[i][0],results[i][1]:results[i][2]]) else 0 for i in range(len(results))])
print('part 1: ',sum)