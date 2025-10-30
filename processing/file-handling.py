from pathlib import Path

# list directories
  # do these directories contain dcm files ? 
    # if yes, put this in a list
  # Create a dictionary of directories as keys and list of dcm files as values

directory = Path('./kagglehub')

# Recursive files search
# - Need checks for empty directories
# -   
def get_files(dir: Path):
    for item in dir.iterdir():
        if item.is_file():
            print(item)
        else:
            get_files(item)

# list the directories within kagglehub
for item in directory.iterdir():
    if item.is_dir():
        get_files(item)
    
    




