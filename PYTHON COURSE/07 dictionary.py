print("Hello World")
print("Dictionary")
d1 = {
    'name':'huzaima', 'age':20, 'degree':'cs', 10:4 ,
    'f1':'usman','f2':'ali',
    'education':['matric','fsc','cs']
}
print("d1=  ",d1)
print("-" * 40)

print("Addition of new key")
d1['f3'] = 'ashan'
print(d1)

print("update of new key")
d1['f3'] = 'adil'
print(d1)

print("deletion of new key")
del d1['f3'] 
print(d1)

print("-" * 40)

print("Methods in Dictionary")
d = d1.get('age' , 'age key not present')
print(d)
print("-" * 40)

d = d1.keys()
print(d)
print("-" * 40)

d = d1.items()
print(d)
print("-" * 40)

d = d1.pop('f2' , 'age key not present')
print(d)
print(d1)
print("-" * 40)

d = d1.popitem()
print(d)
print(d1)
print("-" * 40)

d = d1.clear()
print(d)
print(d1)
print("-" * 40)
print("-" * 40)

print('Comprehensive Dictionary')
d2 = {  i:i+i for i in range(1,11)  }
print(d2)
print("-" * 40)

print("NESTED Dictionary")
d3 = { 
    'student_1':{'name':'huzaima', 'age':20, 'degree':'cs', 10:4 },
    'student_2':{'name':'usman', 'age':21, 'degree':'oversease', 10:4 },
    'student_3':{'name':'adil', 'age':22, 'degree':'cs', 10:4 },
    'd1': d1, 
}
print(d3)
print("-" * 40)

print("loops in Dictionary")
print("-" * 40)
for k in d1:
    print(k)
print("-" * 40)

for k in d1.values():
    print(k)
print("-" * 40)

for k in d1.items():
    print(list(k))
print("-" * 40)








