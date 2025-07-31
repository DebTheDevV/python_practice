with open("harry.txt" , "r") as f :
    content = f.read()
    print(content)

#  no need tp write f.close() as file is already closed by default using with syntax ; even if there is error the file is automatically closed

