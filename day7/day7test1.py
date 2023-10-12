import random
#假设生成随机整数范围为1-100
with open("randonnum.txt","w")as file:
    for _ in range(10):
        random_nun=[str(random.randint(1,100)) for _ in range(3)]
        line=",".join(random_nun)
        file.write(line+"\n")
with open("randonnum.txt","r")as file:  
    second_data=[]
    for line in file:
        pure_line=line.strip().split(",")
        second_data.append(int(pure_line[1]))
max_value=max(second_data)
min_value=min(second_data)
average_value=sum(second_data)/len(second_data)
sorted_value=sorted(second_data)
n=len(second_data)
if n%2==0:
    median_value=(sorted_value[n//2-1]+sorted_value[n//2])/2
else:
    median_value=sorted_value[n/2]
print(f"最大值: {max_value}")
print(f"最小值: {min_value}")
print(f"平均值: {average_value}")
print(f"中位数: {median_value}")
   
    
        