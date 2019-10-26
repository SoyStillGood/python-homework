import os, sys
path = "C:/Users/zachz/Desktop"
dirs = os.listdir(path)
print(dirs)

for file in dirs:
    if os.path.isfile(file) is True:
        print(file, 'file')
    else:
        print(file, 'directory')