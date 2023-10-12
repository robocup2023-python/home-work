list=[]
n=int(input("n=:"))
for i in range(n):
    list.append(int(input()))
m=int(input("m=:"))
for i in range(m):
    temp=list.pop(-1)
    list.insert(0,temp)
print(list)