import os # for interacting with the file system
import shutil #to move files between directions

#define file categories and their corresponding extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Data': ['.csv', '.json', '.xml', '.yaml'],
    'Others': []  # for uncategorized files
}

def organize_files(directory):
    """
    Organizes files in the given directory by their file types.
    """
    
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    #Create folders for each category if they don't exist
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)
        
    #Move files into the appropriate folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        #Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        #check file extension and move to corresponding folder
        file_moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, filename))
                file_moved = True
                break
            
        #Move to "Others" if no category matched
        if not file_moved:
            shutil.move(file_path, os.path.join(directory, 'Others', filename))
            
        print(f"Files in '{directory}' have been organized.")

directory_to_organize = input("Enter the path of the directory to organize: ")
organize_files(directory_to_organize) #call the function to organize files

