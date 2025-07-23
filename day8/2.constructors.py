class Employee :
    # this is the constructor here
    def __init__(self , salary , name , bond):
        self.salary = salary # create an instance attribute of name salry and assign it with salary
        self.name = name
        self.bond = bond 
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of the  employee is {self.name}. Salary is {self.salary} and the bond is for {self.bond} years")
    
e1=Employee(45000 ,"debs" , 4)
print(e1.get_salary())
print(e1.get_info())
