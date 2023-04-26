nums= [1,5,2,4,1]

#method 1

# a= nums[0]
# c=0
# for i in range(len(nums)-1):
#     b= nums[i+1]
#     if len(nums)==1:
#         print(0)
#     else:
#         while a>=b:
#             b+=1
#             c= c+1
#         a=b
#
# print(c)

#method 2
a= nums[0]
b=0
for i in range(1, len(nums)):
    if len(nums)==1:
        print(0)
    else:
        if nums[i]<= a:
            d= abs(nums[i]-a)+1
            b=b+d
            a=nums[i]+d

        else:
            a=nums[i]

print(b)


