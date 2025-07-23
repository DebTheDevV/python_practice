#class is nothing but a blueprint ...,.object is instance of a class

class Employee:
    company = "HP"

    # it is mandatory to give the first paramater as self to all the functions we r creating inside the class


    def get_salary(self): #self basically refers to the object of the class which is being created
        print(self)
        return 34000 
    
e1= Employee ()
#an onj of class employee is created here

print(e1.get_salary()) # employee e's get salary method is called



e2 = Employee()

print(e2.get_salary())

print(e2.company)



