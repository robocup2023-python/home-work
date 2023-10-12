import random
import string
import shutil
def generate_random_string(length):
    character=string.printable.strip()
    return " ".join(random.choice(character)for _ in range(length))
def create_random_file(file_name,l):
    with open(file_name,"w")as file:
        for _ in range(l):
            file.write(generate_random_string(random.randint(1,100))+"\n")
def copy_file(old_file,new_file):
    shutil.copy(old_file,new_file)
if __name__ =="__main__":
    l=int(input("l=:"))
    create_random_file("test.txt",l)
    copy_file("test.txt","copy_test.txt")