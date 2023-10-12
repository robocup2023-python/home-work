num=[0,1]
for i in range(2,20):
    num.append(num[i-1]+num[i-2])
print(num)