words = ["leetcode","win","loops","success"]

pref = "code"

c=0
for i in words:
    if pref in i[0:len(pref)]:
        c+=1

print(c)
