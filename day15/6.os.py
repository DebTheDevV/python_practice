import os

a= os.listdir("dir1")  # shows list of all the directories and files in  the directory
print(a) 

print(os.getcwd())  # get the whole  path of the directory we r in

print(os.path.exists("dir1")) 
# Test whether a path exists. Returns False for broken symbolic links
print(os.path.exists("harry")) 

# os.remove( "del.txt") 
# to delete to a file.. throws error when  the file is not present

os.rmdir("dir2") 
#to delete directory
