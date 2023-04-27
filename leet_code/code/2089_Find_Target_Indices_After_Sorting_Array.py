nums = [1,2,5,2,3]
target = 2

nums= sorted(nums)

c=[]
for i in range(len(nums)):
    if target==nums[i]:
        c.append(i)

print(c)