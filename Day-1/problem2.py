# Implement os Module
import os

# specify the directory path
directory_path = '/'

try:
    # get list of files and directories
    contents = os.listdir(directory_path)

    # print the contents
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The directory does not exist.")
except PermissionError:
    print("Error: Permission denied to access this directory.")
except Exception as e:
    print("An error occurred:", e)
