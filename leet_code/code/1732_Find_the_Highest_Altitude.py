gain = [-4,-3,-2,-1,4,3,2]

a=0
c=[]
for i in range(len(gain)):
    a=a+gain[i]
    c.append(a)

if max(c)<0:
    print(0)
else:
    print(max(c))


