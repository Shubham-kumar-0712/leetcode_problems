nums = [3,2,5,6,3,3,4]

d={}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
l=[]
c=0
for key,value in d.items():
    c+= int(value/2)
    if value%2 !=0:
        l.append(key)

print([c,len(l)])




