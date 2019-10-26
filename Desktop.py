import os, sys
path = "C:/Users/zachz/Desktop"
dirs = os.listdir(path)
print(dirs)

IsFile = []
for file in dirs:
    if os.path.isfile(file)==True:
        IsFile.append(file)
    else:
        print(file, 'directory')

print(IsFile)