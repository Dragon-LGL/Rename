import os

file_dir = "E:\"

files = os.listdir(file_dir)
# print(files)
for file in files:
    filename = file
    # print(filename)
    newname = os.path.splitext(file)[1]
    if filename.find('.pdf') >= 0 :
        newname = filename.replace('.pdf', '.mp4')  #更改的后缀名
        # print('newname:', newname)
    old_path = os.path.join(file_dir, filename)
    new_path = os.path.join(file_dir, newname)
    os.rename(old_path, new_path)

print('Replace Success')
