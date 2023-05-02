startTime = [4]
endTime = [4]
queryTime = 4
c=0

for i in range(len(startTime)):
    if startTime[i]<=queryTime and endTime[i]>=queryTime:
        c+=1

print(c)