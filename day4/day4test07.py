list=[]
for i in range(1,234):
    list.append(i)
index=0
while len(list)>1:
    index=(index+2)%len(list)
    list.pop(index)
print(list[0])