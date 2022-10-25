import os

# Get the list of all files and directories
path = "C://Users//meoho//Downloads//Drugs_5//image"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)


# Rename all files and change it with new name with iterator
for i in  range(0,len(dir_list)):
    old_name = f"C://Users//meoho//Downloads//Drugs_5//image//{dir_list[i]}"
    new_name = f"C://Users//meoho//Downloads//Drugs_5//image//{i+606}.jpg"

    os.rename(old_name, new_name)