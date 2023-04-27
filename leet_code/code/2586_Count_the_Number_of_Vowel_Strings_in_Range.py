words = ["si"]
left = 0
right =0

c = 0
if left==right:
    words=words[left]
    print(words)
    if words[0] in ('a','e','i','o','u') and words[len(words)-1] in ('a','e','i','o','u'):
        c+=1

else:
    words= words[left:right+1]
    print(words)
    for i in words:
        if i[0] in ('a','e','i','o','u') and i[len(i)-1] in ('a','e','i','o','u'):
            c+=1

print(c)