
print("LIST AND TUPLES")
l1 = [1,2,3,4,5,"helo", 'worlds',True]
l2 = [6,7,8,9,10,3,'ki hall a',False]
l3 = list((1.1,5.5,1.2,1,3,1.4,1.5))
l6 = l1.copy()

print("range method")
l4 = list(range(1,6,1))

print('comprehensive method')
expression for i in range(1,1,1) if condition
l5 = [i**2 for i in range(1,11) if i%2==0]
print(l1,l2,l3,l4,l5)

print("access list")
# by index
l0=l1[0]
print(l0)

# update
l6[0] =11
print(l6[0])

# multiple update 
l6[0:3] = 11,22,33 
print(l6)

# concatination
print(l1+l2)

# repition
print(l6*2)

print("mebership function")
inp = int(input("enter a number= "))
if inp in l1:
    print("yes number found")
if inp not in l1:
    print("number not found")

print("alies and clonning")

l7 = l1
l7[0] = 444
print(l1,"------- ",l7)
# it change th l1 value also

l7 = l1.copy()
l7[0] = 10101
print(l1,"------- ",l7)
# it change the l7 value 


print("methods in LIST")
# add at last
l1.append('append')
print(l1)

# add l2 in l1
l8 = l1.extend(l2)
print(l1)

# insert at index
l1.insert(0, 'insert')
print(l1)

# del from index
l1.pop(0)
print(l1)

# remove from element
l1.remove(1)
print(l1)

# find on index
l8 = l1.index('helo')
print(l8)

# count the e
l8 = l1.count(2)
print("sdfgh",l8)

# sort thr list
l9= [1,6,2,7,4,98,45,2,4]
l9.sort()
print("sort ",l9)

l1.reverse()
print(l1)


finding functions
print(min(l3))
print(max(l3))

# common  elements
s1= set(l1)
s2= set(l2)
s3 = s1.intersection(s2)
print("intersection = ",list(s3) )

# nested lists
l8 = [1.3,4,6,8,'567',l1,l2,l3,[1.3,5,4,5,6,"fghj"]]
print(l8)








