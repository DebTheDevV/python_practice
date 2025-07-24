class Employee:
    company = "HP"
    def __init__(self , name , salary):
        self.name= name
        self.salary=salary
 
    #  instance method or the default method :
    def print_info(self):
        print(f"the name is {self.name} and salary is {self.salary}")
    
    def sum(a , b):
        return a+b
    
    #static method
    @staticmethod  # method that doesnt need slef , so self wont be automatically passed when we call the method

    def SUM(a , b):
        return a+b
    
    #class Methods -
    
    @classmethod
    def print_company(cls):
            print(cls.company)

    @classmethod
    def change_company(cls , new_company):
            cls.company=new_company


e1=Employee("jack" , 60000)
e2=Employee("jack" , 65000)

print(Employee.company)
# print(Employee.name) - wiill through an error

# print(e2.sum(2 , 3)) # Python expects self (an instance) as the first argument — but you’re passing two numbers directly.......i can always solve the problem by writing self in this-- def sum(self ,a , b): ... but we dont want to do it as  self here is e2 , which is kind of a heavy object ...SO WE CALL THE STATICMETHOD 

print(e2.SUM(3 , 2))
e1.print_company()

print(Employee.company)
e1.change_company("Acer") #this changes the actual class attributes
e1.print_company() #>>Acer

print(Employee.company) #>>Acer

        