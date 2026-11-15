
import os
from pathlib import Path


class FileManager():

    
    def __init__(self, directory):
        # your folder 
        self.directory = directory
    

    def write_file(self, name, text):
        
        # Create the folder if it doesn't exist (no error if it does)
        os.makedirs(self.directory, exist_ok=True)
        
        # Build the full path, e.g. "my_folder/notes.txt"
        file_path = os.path.join(self.directory, name)
        
    
        # "w" creates the file, or overwrites it if it already exists
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
        
            
    def read_file(self,  name):
        
        file_path = os.path.join(self.directory, name)
        
        if not os.path.isfile(file_path):
            return None
                
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
        

    def list_files(self):
        # if there is no directory 
        if not os.path.isdir(self.directory):
            return []
        
        # this returns a sorted list of only files 
        return sorted(
            entry for entry in os.listdir(self.directory)
            if os.path.isfile(os.path.join(self.directory, entry))
        )
    
    
    def file_size(self, name):

        file_path = os.path.join(self.directory, name)
        
        if not os.path.isfile(file_path):
            return None
        
        file_size = os.path.getsize(file_path)
        
        return file_size
        
    
    def delete_file(self, name):
        
        file_path = os.path.join(self.directory, name)
        
        try:
            os.remove(file_path)
            return True 
        except FileNotFoundError:
           return False 
            
        

fm = FileManager("my_folder")
fm.write_file("notes.txt", "hello world")
fm.write_file("todo.txt", "buy milk")
print(fm.list_files())
print(fm.read_file("notes.txt"))
print(fm.file_size("todo.txt"))
print(fm.delete_file("notes.txt"))
print(fm.delete_file("notes.txt"))
print(fm.list_files())
print(fm.read_file("missing.txt"))
    
    
    
# ['notes.txt', 'todo.txt']
# hello world
# 8
# True
# False
# ['todo.txt']
# None