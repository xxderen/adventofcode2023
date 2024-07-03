from functools import reduce
from math import lcm
#Test
instruction, network = open('day8_input.txt').read().split('\n\n')
network = network.split('\n')

a=[i[0:3] for i in network] #Current location
b=[i[7:10] for i in network] #Left
c=[i[12:15] for i in network] #Right

#Part 1
start = "AAA"
count = 0
while start != "ZZZ":
    for direction in instruction:
        if direction == "R":
            start = c[a.index(start)]
        else:
            start = b[a.index(start)]
        count += 1
        if start == "ZZZ":
            print(count)

#Part 2
allnode=[i for i in a if i[2]=='A']
count=0
z=0
y=[]
e=len(allnode)
while z<e:
    for direction in instruction:
        for i in range(len(allnode)): 
            if direction == "L":
                allnode[i] = b[a.index(allnode[i])]
            else:
                allnode[i] = c[a.index(allnode[i])]
        count += 1
        for x in allnode:
            if x[2]=='Z':
                z+=1
                allnode.remove(x)
                y.append(count)
print(reduce(lcm,y))
