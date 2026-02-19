from pathlib import Path
import shutil

path = Path('G:/Google Takeout/takeout-20260102T230411Z-3-007/Takeout/Google Photos/Test')
outPathPrefix = Path('G:/Google Takeout/')
splitindexes = [4, 6]

def moveFiles(item: Path):    
    '''
    1. Split the item (file)
    2. Specify folder name 
    3. The 'rename' call basically transfers the file to the new location
    '''
    print(item)
    fileString = str(item).split('_')[1]
    folderName = '2023-' + fileString[4:6]
    print(folderName)    
    Path(item).rename(Path(str(outPathPrefix),folderName,item.name))
    

def get_files(dir: Path):
    print('What is happening')
    for item in dir.iterdir():
        if item.is_file():
          moveFiles(item)  
        else:
            get_files(item)


get_files(path)