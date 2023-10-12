x=[]
y=[]
print("输入第一个矩阵")
for i in range(3):
    row=[]
    for j in range(3):
        element=int(input())
        row.append(element)
    x.append(row) 
print("输入第二个矩阵")  
for i in range(3):
    row=[]
    for j in range(3):
        element=int(input())
        row.append(element)
    y.append(row)
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        res[i][j]=x[i][j]+y[i][j]
for row in res:
    print(row)