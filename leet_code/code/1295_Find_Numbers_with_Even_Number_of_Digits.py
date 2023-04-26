nums = [12,345,2,6,7896]

nums= list(map(str,nums))
c=0
for i in nums:
    if len(i)%2==0:
        c+=1
print(c)