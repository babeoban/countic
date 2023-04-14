import os
import time

# specify the file paths as a list
file_paths = ["nether.txt", "stronghold.txt", "edn.txt", "bastion.txt", "fortress.txt", "blind.txt", "dragon.txt"]

# iterate over the file paths and delete each file
for file_path in file_paths:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    else:
        print(f"File {file_path} not found.")

time.sleep(1.5)
