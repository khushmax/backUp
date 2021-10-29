import os
import shutil

source = input("enter the source name of the source folder :")
destination = input("enter the destination name of the destination folder :")

source = source + "/"
destination = destination + "/"

print(source)
print(destination)

listOfFiles = os.listdir(source)

# in the first file in listOfFile(python) it will copy it and put it in the destination file 
for file in listOfFiles:
    shutil.copy((source + file), destination)

