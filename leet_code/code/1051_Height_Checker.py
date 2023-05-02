heights = [5,1,2,3,4]

h= sorted(heights)
c=0

for i in range(len(heights)):
    if heights[i]!=h[i]:
        c+=1

print(c)
