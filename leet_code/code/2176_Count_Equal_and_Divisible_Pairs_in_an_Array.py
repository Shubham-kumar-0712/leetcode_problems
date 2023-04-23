import math
nums = [3,1,2,2,2,1,3]
k = 2
# c=[]
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i]==nums[j]:
#             if i!=j and j>i:
#                 c.append([i,j])
# d=0
# for i in c:
#     if math.prod(i)%k ==0:
#         d+=1
#
# print(d)

cnt = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            if i*j % k == 0:
                cnt += 1

print(cnt)

