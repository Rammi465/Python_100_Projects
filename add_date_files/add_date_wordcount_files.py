import os
from datetime import datetime 

#specify the diectory wheere the files are located
directory = 'add_date_wordcount_files/files'

#get a list of file names in the specified directory
filenames = os.listdir(directory)

#loop through each file in the directory
for filename in filenames:
    #construc the file path
    filepath = os.path.join(directory, filename)
    
    #Ge the cueent date in MM-DD-YYYY format
    current_date = datetime.now().strftime("%Y-%m-%d")
 
       
   #Modify the file name with date        
    new_filename = f'{filename[:-4]}-{current_date}.txt'
    
    #Construct the the new full file path with updated file name
    
    new_filepath = os.path.join(directory, new_filename)
    
    #rename the original file with new file name
    os.rename(filepath, new_filepath)
    
    #Print message indicating the rename of file
    print(f"Renamed {filename} to {new_filename}")
    
print("Renaming is is successful")