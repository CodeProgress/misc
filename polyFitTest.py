import pylab

pos     = []
posTemp = []

for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if i+j+k <= 9:
                pos.append([i,j,k])


vals = [len(pos)]

def extend_last_two(aList):
    """aList = [a,b, ..., x,y] returns possible successors, [a,b .., x,y,z]
    for all z"""
    lastTwoTotal = aList[-2] + aList[-1]
    maxZ = 9 - lastTwoTotal
    return [aList + [z] for z in range(maxZ + 1)]

for i in range(5):
    for i in pos:
        for j in extend_last_two(i):
            posTemp.append(j)

    pos = posTemp
    posTemp = []
    vals.append(len(pos))
    
x = pylab.array([3,4,5,6,7,8])
y = pylab.array(vals)
z = pylab.polyfit(x, y, 2)


