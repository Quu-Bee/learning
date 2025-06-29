import os
import json
import shutil
from pathlib import Path
from filter_file import filter_files

with open('C:/Users/Я/Documents/Sanya_IT/file_organizer/filters.json', 'r') as f:
    subfolder_filter = json.load(f)

all_extentions = [ext for extentions in subfolder_filter.values() for ext in extentions]
os.chdir("C:/Users/Я/Downloads")
directory = os.listdir()
for name in subfolder_filter:
    if name not in directory:
        os.mkdir(name)
filter_files(directory, all_extentions)

categorized_files = {category: [] for category in subfolder_filter}
for file in filter_files(directory, all_extentions):
    path = Path(file)
    ext = path.suffix
    for category, extensions in subfolder_filter.items():
        if ext[1:] in [e.lower() for e in extensions]:
            categorized_files[category].append(file)

for category, file_name in categorized_files.items():
    for file in file_name:
        if file_name != []:
            source = f"C:/Users/Я/Downloads/{file}"
            destination_folder = f"C:/Users/Я/Downloads/{category}/{file}"
            shutil.move(source, destination_folder)


