import os

#get current working directory 

current = os.getcwd()
print("Current Working dir",current)

# print directory tree

dir_struct = os.walk(".")

for dir_path,dir_names,file_names in dir_struct:
	print("Dir Path",dir_path)
	print("Dir Name",dir_names)
	for name in file_names:
		full_name = name.split(".")
		print("File Name ->", full_name[0])
		print("Extension ->", full_name[1])
	print("-------------")
