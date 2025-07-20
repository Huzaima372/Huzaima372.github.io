print("hello worlf")
print("Functions in python")

def greet():
    print("ki haal aa dosto ki gal aa mahool sai ni bnya")

greet()

###########################################################
def add(x,y,n):
    adds=x+y
    print (adds , n)
    return adds
    
a = add(2,3,"hassan")
print("add " , a)

###########################################################
# arguments

# positional arg
# position notes
add(1,2,"hello")

# keyword arg 
add(x=3,y=3, n="aneeq")

# default arguments
def add(x=2,y=1,n='ali'):
    adds=x+y
    print (adds , n)
    return adds
add()

###########################################################
# Decorators
def my_dec(func):
    def ins():
        print("you entered in decoration section............ ")
        func()
        print("your function runs sucessfully......")
    return ins
    
@my_dec
def load():
    print("load function")
    
load()
    
###########################################################
def generator(num):
    while num>0:
        yield num
        num -=1

for n in generator(10):
    print(n)

    
###########################################################

add_ten = lambda x:x+10
print(add_ten(20))
    

###########################################################    
    
    
    
    





