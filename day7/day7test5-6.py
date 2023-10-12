import os
import day7test2
if not os.path.exists("test"):
    os.mkdir("test")
i=int(input("i=:"))
j=int(input("j=:"))
def create_random_files(i):
    for k in range(i):
        with open(os.path.join("test", f"test{k}.txt"),"w")as file:
            file.write(day7test2.generate_random_string(j))
def traverse():
    for filename in os.listdir("test"):
        if filename.endswith(".txt"):
            file_path=os.path.join("test",filename)
            new_filename=filename.replace(".txt","-python.txt")
            new_file_path=os.path.join("test",new_filename)
            with open(file_path,"r")as file:
                lines=file.readlines()
            with open(new_file_path,"w")as file:
                for line in lines:
                    file.write(line.strip()+"-python\n")
def change():
    for filename in os.listdir("test"):
        file_path=os.path.join("test",filename)
        if "python" in filename:
            new_filename=filename.replace("python","class")
            new_file_path=os.path.join("test",new_filename)
        with open(new_file_path,"r")as file:
            content=file.read()
            if "python" in content:
                content=content.replace("python","class")
        with open(new_file_path,"w")as file:
            file.write(content)