#initiate a class 

class employee:
    #special methods/function method /dunder method -constructor
    def __init__(self):
        print("Started execting attribute or data")
        self.id = 123
        self.salary = 50000
        self.designation = "Software Engineer"
        print("attribute and data have been initiated")

    # when we define function inside class then it called method
    def travel(self,destination):
        print("This travl function was called manually")
        print("Employees is now travelling to ",destination)


#creating an object/inctence of the class 
sam =employee()
#calling a method
#sam.travel("moon")

#print(sam.id)
print(type(sam))