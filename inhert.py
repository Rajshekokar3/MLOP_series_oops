# Base class
'''class Animal:

    def __init__(self,name): #Constructore
        self.name=name

    def speak(self):
        print(f"{self.name} makes a sound")
    


#animal=Animal("Genreic Animal Sound")
#animal.speak()


#Derived class 
class Dog(Animal): #for derived class we are giving the whole class as sa argumnt to the new class called child class
    
    def __init__(self,name):
        self.behaviour="friendly"



    def speak(self):  #Overriding the function 
        print(f"{self.name} barks .He is very {self.behaviour}")


dog =Dog("Buddy")
dog.speak()'''

#super keyboard


class Animal:
    def __init__(self):
        self.name="Buddy"

    def spak(self):
        print(f"{self.name} makes a sound. ")

    
class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed=breed

    def speak(self):
        self.spak() # if the method is same than super is used to indicate that thhe this method is parents class method 
        print(f"{self.name} barks.It is a {self.breed}")


#Create an instance of Dog
dog=Dog("Golden retrive")
dog.speak()