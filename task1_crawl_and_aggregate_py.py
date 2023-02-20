import os

ROOT = "repos_in"
OUTFILE = "all_python.txt"

python_files = []
for root, subdirs, files in os.walk(ROOT):
    for file in files:
        if file[-3:] == ".py":
            python_files.append(root + "/" + file)


with open(OUTFILE, "w+") as outfile:    
    for pyf in python_files:
        print(f"adding {pyf} to output")
        with open (pyf, "r") as infile:
            lines = infile.readlines()
            outfile.writelines(lines)
