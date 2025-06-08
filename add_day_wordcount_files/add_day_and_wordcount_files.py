import os
from datetime import datetime

directory = 'add_day_wordcount_files/files'
filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory, filename)
    
#print(filepath)
    with open(filepath, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        #print(word_count)
        
    
    day = datetime.now().strftime("%A")
    new_filename = f'{filename[:-4]}-{word_count}-{day}.txt'
    
    new_filepath = os.path.join(directory, new_filename)
    os.rename(filepath, new_filepath)
    
    print(f"Renamed {filename} to  {new_filename}")
