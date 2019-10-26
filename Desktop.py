import os, sys
path = "C:/Users/zachz/Desktop"
dirs = os.listdir(path)
print(dirs)

for file in dirs:
    print(file, 'file')
for dir in dirs:
    print(dir, 'directory')