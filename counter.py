DIR_NAME_HERE = "."
IGNORE = [
    ".git",
    ".vscode",
    "node_modules",
    "build",
    "dist",
    "key"
]
LISENCE = 674
import os
global total_count
total_count = 0
def file_len(fname):
    global total_count
    cnt = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            cnt+=i
    total_count += i + 1
    return i + 1
def looper(dir_name):
    global total_count
    files = os.listdir(dir_name)
    for fd in IGNORE:
        for f in files:
            if fd == f:
                files.remove(fd)
    for f in files:
        if os.path.isdir(dir_name + "/" + f) == 1:
            new_dir = dir_name + "/" + f 
            looper(new_dir)
        else:
            try:
                print(dir_name + "/" + f + ": " + str(file_len(dir_name + "/" + f)))
            except:
                print(dir_name + "/" + f + " is not readble.")
looper(DIR_NAME_HERE)
print("Total Line Count of root folder '" + DIR_NAME_HERE + "/': " + str(total_count - LISENCE))
