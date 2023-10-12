import day7test2
l=int(input("l=:"))
day7test2.create_random_file("test.txt",l)
day7test2.copy_file("test.txt","copy_test.txt")
with open("test.txt","r")as file:
    content=file.read()
    content="python"+content
    content+="python"
with open("test.txt","w")as file:
    file.write(content)
with open("test.txt")as file1,open("copy_test.txt")as file2:
    line1=file1.readlines()
    line2=file2.readlines()
line_min=min(len(line1),len(line2))
line_max=max(len(line1),len(line2))
diff=[]
for i in range(len(line_min)):
    if line1[i]!=line2[i]:
        diff.append(i)
if len(line1)==len(line2):
    if diff:
        print(diff)
    else:
        print("文本内容相同")
else:
    if diff:
        diff.append(range(line_min+1,line_max+1))
        print(diff)
    else:
        print(range(line_min+1,line_max+1))
        
