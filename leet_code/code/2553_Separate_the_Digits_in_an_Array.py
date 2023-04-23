nums = [13,2508,83,77]
l=[]
for i in nums:
    length= len(str(i))
    b=[]
    while length!=0:
        a=int(i)%10
        b.append(a)
        i=i/10
        length= length-1
    b.reverse()
    l.append(b)

c= [j for i in l for j in i]

print(c)

# final = []
# for a in nums:
#     for b in str(a):
#         final.append(int(b))
#
# print(final)
# b= str(nums)
# c=[]
# c.append(b)
# print(c)








