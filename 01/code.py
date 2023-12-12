import numpy as np
with open('text.txt') as f:
    lines = f.readlines()
#part 1
numbers =[ list(filter(lambda x: x.isdigit(), [*line])) for line in lines]
numbersfiltered = [num[0]+num[-1] for num in filter(lambda x :len(x)>0,numbers)]
print('part 1 :' ,np.sum([int(n) for n in numbersfiltered]))


#part 2
valid_digits=['one','two','three','four','five','six','seven','eight','nine']
for dig,textvalue in enumerate(valid_digits):
    lines=[line.replace(textvalue,textvalue+str(dig+1)+textvalue) for line in lines]

numbers =[ list(filter(lambda x: x.isdigit(), [*line])) for line in lines]
numbersfiltered = [num[0]+num[-1] for num in filter(lambda x :len(x)>0,numbers)]
print('part 2 : ',np.sum([int(n) for n in numbersfiltered]))