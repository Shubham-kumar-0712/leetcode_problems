nums = [2,1,2,5,3,2]

a= set(nums)
c=0
for i in a:
    for j in nums:
        if i==j:
            c+=1
    if c==len(nums)/2:
        print(i)
    c=0
