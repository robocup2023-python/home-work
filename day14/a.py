import os
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter
import csv
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper

def count_words_in_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    w_elements = root.findall(".//w")
    text_contents = [element.text for element in w_elements]
    count=Counter(text_contents)
    return count

def process_files_with_thread(file_paths, num_threads_per_process):
    thread_results = []
    with ThreadPoolExecutor(max_workers=num_threads_per_process) as executor:
        for file_path in file_paths:
            words = list(executor.map(count_words_in_xml, [file_path]))
            thread_results.extend(words)
    return thread_results

@timing_decorator
def process_files_with_processes(file_paths, num_processes, num_threads_per_process):
    results = []
    chunk_size = len(file_paths) // num_processes
    process_chunks = [file_paths[i:i + chunk_size] for i in range(0, len(file_paths), chunk_size)]

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        for chunk in process_chunks:
            results.extend(list(executor.map(process_files_with_thread, [chunk], [num_threads_per_process] * len(chunk))))
    return results
@timing_decorator
def generate_csv(data, file):
    all_words = [word for lists in data for words in lists for word in words]
    word_counts = Counter(all_words)
    
    with open(file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Word", "Count"])
        csv_writer.writerows(word_counts.items())
if __name__ == "__main":
    file_paths=[]
    folder_paths=['/home/robocup/Downloads/第十四天附件/download/Texts/dem','/home/robocup/Downloads/第十四天附件/download/Texts/news','/home/robocup/Downloads/第十四天附件/download/Texts/aca','/home/robocup/Downloads/第十四天附件/download/Texts/fic']
    for folder in folder_paths:
        file_paths.extend([os.path.join(folder, filename) for filename in os.listdir(folder) if filename.endswith(".xml")])
    process_results = process_files_with_processes(file_paths, num_processes=16, num_threads_per_process=32)
    generate_csv(process_results, "process_results.csv")
    