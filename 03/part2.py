import numpy as np
import re

with open('./data.txt') as f:
    lines = f.readlines()

lines = [l.replace('\n','') for l in lines]
chars=[[c for c in line] for line in [*lines]]
results=[]
# find numbers
for n,line in enumerate(lines):
    p    = re.compile("[0-9]+")
    for m in p.finditer(line):
             results.append([n,m.start(),m.end(),m.group()])
             
numbers_matrix=np.zeros((140,140))
diffnum=np.zeros((140,140))
for i,r in enumerate(results):
     numbers_matrix[r[0],r[1]:r[2]]=r[3]
     diffnum[r[0],r[1]:r[2]]=i+1
# calculate sum
sum=0
for l in range(140):
      for k in range(140):
             if chars[l][k] == '*':
                   done=[]
                   numbers=[]
                   num=np.array(numbers_matrix[l-1:l+2,k-1:k+2]).flatten()
                   diffnum_=diffnum[l-1:l+2,k-1:k+2].flatten()
                   if len(np.unique(diffnum_)) ==3:
                         for ii in range (len(diffnum_)):
                               if done.count(diffnum_[ii])<1:
                                     done.append(diffnum_[ii])
                                     if num[ii]>0:
                                          numbers.append(num[ii])
                         sum+=numbers[0]*numbers[1]
                
print('part 2: ',sum)