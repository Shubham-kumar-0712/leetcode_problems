words = ["abc","car","ada","racecar","cool"]

c=[]
for i in words:
    if i==i[::-1]:
        c =i
        break

if len(c)==0:
    print("")
else:
    print(c)


