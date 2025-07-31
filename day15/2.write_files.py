# write to a file called John Doe. txt 
# it shud contain data about John Doe 

f= open("John Doe .txt" , "w")

string='''
John Doe is a nice guy ... he lives in NYC and  he works with Python .. 
His favourite package is Pandas 
'''
f.write(string)
f.close()