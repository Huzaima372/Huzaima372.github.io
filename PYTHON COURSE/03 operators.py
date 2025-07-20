print("operators in py")

x = 10
y = 5
z = 20
a = None
size = True

veg = ['tomaot', 'bhindi', 'karela']

print('arithmatic operator')
a = x + y
print("add = ",a)
a = x - y
print("Subtract = ",a)
a = x * y
print("Multiply = ",a)
a = x / y
print("Division = ",a)
a = x ** y
print("power = ",a)
a = x % y
print("remainder = ",a)


print('comparison operator => boolean value') 
a = x < y
print("Less = ",a)
a = x > y
print("Greater = ",a)
a = x <= y
print("less equal = ",a)
a = x >= y
print("greater equal = ",a)
a = x == y
print("equal to = ",a)
a = x != y
print("not equal = ",a)

print('logical operator')

if ((x == 10) and (y == 54)):
 {print("and = ",a)}
else:
 {print("and false ",a)}

if ((x == 10) or (y == 54)):
 {print("or = ",a)}
else:
 {print("or false ",a)}

    # print( not(a==2))


print('assignment operator')
print(x==a)
x += y
print(x)
x-= y
print(x)
x *= y
print(x)
x /= y
print(x)



print('identity operators => memory location')
print(a is a)
print(x is y)
print(y is z)
print(size is size)



print("membership operator => value exist or not")
print('tomaot' in veg)
print('potato' in veg)
print('bhindi' in veg)
print("karela" in veg)






