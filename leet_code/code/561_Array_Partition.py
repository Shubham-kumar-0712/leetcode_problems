nums = [1,4,3,2]

a= sorted(nums)
b= len(nums)/2
c=[]
for i in range(0,len(a),2):
    c.append((a[i],a[i+1]))

d= list(map(min,c))
e= sum(d)
print(e)



