a=int(input("a=:"))
n=int(input("n=:"))
res=0
for i in range(n):
    temp=str(a)*(i+1)
    res+=int(temp)
print("res=",res)