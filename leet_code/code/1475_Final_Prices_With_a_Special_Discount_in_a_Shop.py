prices = [1,2,3,4,5]

c = []

for i in range(0,len(prices) - 1):
    for j in range(i+1,len(prices)):
        if prices[j]<=prices[i]:
            prices[i]=prices[i]-prices[j]
            break

print(prices)
