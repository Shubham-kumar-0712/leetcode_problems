nums = [1,2,3,2]


a= set(nums)
c=0
d=[]
for i in a:
    for j in nums:
        if i==j:
            c+=1

    if c==1:
        d.append(i)
    c=0

print(sum(d))


