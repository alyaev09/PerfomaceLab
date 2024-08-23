import sys
import math
file_name1 = sys.argv[1]
file_name2 = sys.argv[2]

with open(file_name1) as file:
    circle = file.read().split()
x0 = int(circle[0])
y0 = int(circle[1])
r = int(circle[2])
with open(file_name2) as file:
    for line in file:
        x, y = line.split()
        ro = math.sqrt((int(x) - x0)**2 + (int(y) - y0)**2)
        if ro < 5:
            print(1)
        elif ro > 5:
            print(2)
        else:
            print(0)