print(' CONTROL STATEMENTS')
num1 = int(input("enter a num1= "))
num2 = int(input("enter a num2= "))

print('if statements')
if num1 > 10:
    print('num1 is greater then >>10<< num1= ', num1)

print('if else statement')
if num1 > 10:
    print('num1 is greater then >>10<< num1= ', num1)
else:
    print('num1 is less then >>10<< num1= ', num1)

print('if elif else statement')
if num1 > 10:
    print('num1 is greater then >>10<< num1= ', num1)
elif num1 >=10:
    print('num1 is Equal to >>10<< num1= ', num1)
else:
    print('num1 is less then >>10<< num1= ', num1)
    

print('LOOPS ')
print('while loop')
a = 1
while a <= 10:
    print('loop run a= ',a)
    a = a+1

print('FOR LOOP')
# also on tuple
my_list = [1,2,3,'a','b']
for i in my_list:
    print('my list = ', i)

print('range function')
my_list = list(range(1,11,1))
print(my_list)



print('NESTED LOOP')
for i in range(1,5):
    for j in range(2,4):
        print( (i),(j))

        
print('BREAK statement')
for i in range(1,11):
    if i == 5:
        break
    print('', i)
    
print('continue statement')
for i in range(1,11):
    if i == 5:
        continue
    print('', i)
    
print('PASS statement')
for i in range(1,11):
    if i == 5:
        pass
    print('', i)







