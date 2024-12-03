import os

# List files in a directory
def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f"Files in {directory}:")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory {directory} does not exist.")

list_files("/etc")
