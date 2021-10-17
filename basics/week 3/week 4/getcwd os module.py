# It is often useful to check our current working directory before beginning to work with files so that we can provide appropriate file paths.  We can do this using the method getcwd of the module os which displays the file path of the current working directory.


import os
path = os.getcwd()
print(f"Current Working Directory: {path}")


for file in os.listdir(path):
  print(file)