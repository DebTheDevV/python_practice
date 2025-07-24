#this code shows why we need getter and setter.. like we need to write extra lines of code here..
class Employee :
    def __init__(self , name , salary):
        self.name= name
        self.salary=salary
    def first_name(self):
        """ 
        return self.name.split(" ")[0] is same as-

        l=self.name.split(" ")
        print(l)
        return l[0]
        
        """
      
        return self.name.split(" ")[0]
    
    def last_name(self):
        return self.name.split(" ")[1]
    
    def set_first_name(self , first ):
        l=self.name.split(" ")
        l[0]=first
        new_name=f"{l[0]} {l[1]}"
        self.name=new_name

        
e=Employee("Jack Doe" , 345555)

# e.projects=6
# # You’re dynamically adding a new attribute to the e object after it’s already created.Python allows this by default unless you explicitly restrict it.
# print(e.projects)

print(e.first_name())
print(e.last_name())

e.set_first_name("John")
print(e.name)
        