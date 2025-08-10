#initiate a class 

class employee:
    #special methods/function method /dunder method -constructor
    def __init__(self):
        print(id(self)) # it use toshare the location 
        print("Started execting attribute or data")
        self.id = 123
        self.salary = 50000
        self.designation = "Software Engineer"
        print("attribute and data have been initiated")

    # when we define function inside class then it called method
    def travel(self,destination): # we cant write swithout self beacuse fo after create a object it automatically pass the object to methods
        print("This travl function was called manually")
        print("Employees is now travelling to ",destination)


#creating an object/inctence of the class 
sam =employee()
print(id(sam))
#calling a method
#sam.travel("moon")
sam.name="Raj Shekokar"

print(sam.name)

#print(sam.id)
print(type(sam))