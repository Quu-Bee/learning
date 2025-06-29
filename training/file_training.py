import json
with open("training/file.json", encoding= "utf-8") as file:
    some_dict = json.load(file)
    print(some_dict)
with open("training/file_file.json", "w", encoding= "utf-8") as file:
    json.dump(some_dict, file, ensure_ascii= False)
    


