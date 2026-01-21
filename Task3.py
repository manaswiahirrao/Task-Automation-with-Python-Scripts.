# Task 3: Task Automation
# This program moves all .jpg files from 'source' folder to 'Images' folder

import os
import shutil

source_folder = "source"
destination_folder = "Images"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Check files in source folder
for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(file, "moved successfully")

print("Task Automation Completed!")