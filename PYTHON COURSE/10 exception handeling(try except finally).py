print("=" * 50)
print("exception handling")
print("=" * 50)

################################################
a = 10; b = 2
# erors 
# compile time error 
if a>= b 
    print(a / b)

# runtime error
b = 0
print(a / b)

# logical error
print(f'{a} / {b} = {a/b}')

print("=" * 50)
################################################

# try except 
try:
    a = int(input("Enter a number = "))
    b = int(input("Enter a number = "))
    print(a/b)
    
except ZeroDivisionError :
    print(f'number 2 not be {b}')

print("=" * 50)
################################################

# finally block

try:
    a = int(input("Enter a number = "))
    b = int(input("Enter a number = "))
    print(a/b)
    
except ZeroDivisionError :
    print(f'number 2 not be {b}')
finally:
    print("try except finally exicuted")

print("=" * 50)
################################################

# nested and riasekeyword 
def div(a,b):
    print(a/b)
    raise Exception ("Error not founnd")

try:
    a = int(input("Enter a number = "))
    b = int(input("Enter a number = "))
    div(a,b)
except Exception as e:
    print (e)
    


print("=" * 50)
#################################################
