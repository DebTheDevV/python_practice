# append to an existing file called john Doe.txt 
# it shud add data about john doe's hometown

f=open("John Doe .txt" , "a")

string = """
John Doe initially lived in Phoenix , arizona .. He is a very nice guy
"""

f.write(string)

f.close()


