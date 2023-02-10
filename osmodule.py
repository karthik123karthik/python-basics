import os

path = 'C:/Users/user/Desktop/os module/directory/'
files = os.listdir(path)
for index, file in enumerate(files):
  If file.endsWith(".py"):
    src = path+file
    dest = path+f"{index}.py"
    os.rename(src, dest)
