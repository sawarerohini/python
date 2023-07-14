#directory (folder)
#os getcwd()  --cwd(current working directory)
import os
os.getcwd()               #cwd(current working directory)
print(os.getcwd())
print(os.listdir()) # return list of all file and folder of current directory
print(os.listdir('C:\ROHINI'))

#new directory
os.mkdir("text")
os.mkdir('C:/ROHINI/python_deta/project')     #aneyther location folder creat in your personal drive
print("done")

# 4)rename directory
# old folder name to rename new folder name
os.rename('C:/ROHINI/python_deta/project','C:/ROHINI/python_deta/demo123')

# 5)remove directory
os.rmdir('C:/ROHINI/python_deta/project')
os.remove("text")




