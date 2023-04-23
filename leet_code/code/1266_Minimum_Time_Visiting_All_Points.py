import math
points = [[1, 1], [3, 4], [-1, 0]]

c=[]
for i in range(len(points)-1):
    c.append([abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1])])

d=list(map(max,c))
print(sum(d))






