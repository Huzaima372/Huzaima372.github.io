class car:

##########################################################
by constructor 
    def __init__(self, name, color):
        self.name = name
        self.color = color

# by default constructor
    def __init__(self):
        self.name = name
        self.color = color
        
# by parameterized constructor
    def __init__(self, name, color):
        self.name = name
        self.color = color

# by default value constructor
    def __init__(self, name = "TOYOTA", color = "BABY PINK"):
        self.name = name
        self.color = color

##########################################################
# by object and classes concept
    def set_details(self, name, color):
        self.name = name
        self.color = color
    
##########################################################
    def display(self):
        print(f"{self.name} have {self.color} color")


##########################################################
# by object and classes concept
o1 = car()
o1.set_details("JAC", 'glossy black')
o1.display()

##########################################################
# by constructor 
o1 = car("ROCCO", "mate black")
o1.display()

## by default constructor
o1 = car()
o1.display()

## by parameterized constructor
o1 = car("ROCCO", "mate black")
o1.display()

## by default value constructor
o1 = car()
# o1.display()


##########################################################
print('-' * 50)
print("polymorphism")

class animal:
    def sound(self):
        print("animal sounds")

class dog(animal):
    def sound(self):
        print("dog bark")
        
class cat(animal):
    def sound(self):
        print("cat meaow")

c = cat()
c.sound()
        

##########################################################
print('-' * 50)
print("inheritance")

class animal:
    def sound(self):
        print("animal sounds")

class dog(animal):
    def dog_sound(self):
        print("dog bark")
        
class cat(animal):
    def cat_sound(self):
        print("cat meaow")

c = cat()
c.sound()
c.cat_sound()
        

##########################################################
print('-' * 50)
print("encapsulation")

class bank:
    def __init__(self, num ,ammount):
        self.num = num
        self.__ammount = ammount
        
    def set_ammount(self,add_amount):
        # ammount = 1000
        self.__ammount += add_amount
        print("amount updated with ",add_amount)
    
    def get_ammount(self):
        return self.__ammount
       
c1 = bank(112232, 2000)
c1.set_ammount(1000)
print(c1.get_ammount())

print('-' * 50)


##########################################################

print("=" *50)
print("Abstraction")
 
from abc import ABC , abstractmethod
 
class animal(ABC):
     @abstractmethod
     def sound(self):
         pass
     
class cat(animal):
    def sound(self):
        print("cat meoww")
    

c1 = cat()
c1.sound()
print("=" *50)













