
# Magic or Dunder Methods in Python
# ----------------------------------
# Examples: __init__, __str__, __add__, etc.
#
# These special methods allow you to:
# 1. Customize object creation and initialization (e.g., __new__, __init__)
# 2. Enable operator overloading (e.g., +, -, *, ==, <, > using __add__, __eq__, etc.)
# 3. Provide readable string representation of objects (__str__, __repr__)
# 4. Control attribute access (__getattr__, __setattr__, __delattr__)
# 5. Make objects callable like functions (__call__)
# 6. Implement container-like behavior (__len__, __getitem__, __setitem__, __iter__)
# 7. Support use with context managers (__enter__, __exit__)


class Employee:
    company ="HP" 
    def __init__(self , name , salary):
        self.name = name ; 
        self.salary= salary ; 

    def __str__(self): # mostly used for the user
        return f"The name is {self.name} and the salary is {self.salary}..."
    
    def __repr__(self):#mostly for devOp , who r trynna debug the code !! 
        return f"name : {self.name} \nsalary: {self.salary}..."
    
    def __len__(self):
        return len(self.name)
        

e= Employee ("harry" ,43566 )
print(e.name , e.salary)
print(str(e))
print(repr(e))
print(len(e))