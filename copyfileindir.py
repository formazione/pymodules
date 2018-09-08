import os
import shutil
# from path import path

destination = "F:\\_file_docx"
# os.makedirs(destination)


def copyfile(dir, filetype='docx', counter=0):
    "Searches for pptx (or other - pptx is the default) files and copies them"
    for pack in os.walk(dir):
        for f in pack[2]:
            if f.endswith(filetype):
                fullpath = pack[0] + "\\" + f
                print(fullpath)
                shutil.copy(fullpath, destination)
                counter += 1
    if counter > 0:
        print("------------------------")
        print("\t==> Found in: `" + dir + "` : " + str(counter) + " files\n")


for dir in os.listdir("F:\\"):
    "searches for folders that starts with `_`"
    print(dir)
    copyfile(dir, filetype='docx')
print("end")
