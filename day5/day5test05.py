import os
import random
from day5test04 import path
path()
files=os.listdir("img")
random.shuffle(files)
for i,old_name in enumerate(files):
    new_name=f"X4g{i}.jpg"
    new_path=os.path.join("img",new_name)
    os.rename(path.old_name,new_name)
    