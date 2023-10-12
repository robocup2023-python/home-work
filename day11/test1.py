import os
import threading
def rename(files):
    for old_name,new_name in files:
        os.rename(old_name,new_name)

if __name__ =="__main__":
    files_to_rename=[("file1.txt","new_file1.txt"),("file2.txt","new_file2.txt")]
    num_thread=4
    chunk_size=len(files_to_rename)//num_thread
    threads=[]
    for i in range(num_thread):
        start=i*chunk_size
        end=start+chunk_size if i<num_thread-1 else len(files_to_rename)
        chunk=files_to_rename[start:end]
        thread=threading.Thread(target=rename,arg=(chunk,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
        