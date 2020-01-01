from numpy import random
from pylab import plot,show

yvec = [] # set up an empty vector
for i in range(999): # want 200 numbers
    yy = 25 + 3*random.randn() # normal dist with mean = 15, sd = 2
    yvec.append(yy) # enter yy into vector

plot(yvec)
show(yvec)