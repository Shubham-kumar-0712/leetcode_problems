image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
c=[]
a = list(map(lambda x: x[::-1], image))

def func(x):
    if x == 0:
        return 1
    else:
        return 0

for i in a:
    b = list(map(func, i))
    c.append(b)

print(c)
