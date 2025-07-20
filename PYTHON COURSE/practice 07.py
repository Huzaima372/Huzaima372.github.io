"""
Mini Project – Shopping Cart Manager (C Version)
You are tasked with building a simple shopping cart management system in C.
The program should:
Initialize the shopping cart with these items and quantities:
Apple: 2, Banana: 5 , Milk: 1
Add 3 more bananas to the cart.
Add a new item 'Bread' with quantity 2.
Remove 'Milk' from the cart.
Print all remaining items in the cart along with their quantities.
"""

d1 = {
    "apple": 2, "banana": 5, "milk": 1
}

# first 3 more banana 
d2 = d1['banana']
d2 +=3
print(d2)
d1['banana'] = d2
print(d1)
print('=' * 50)

# new item
d1["bread"] = 2
print(d1)
print('=' * 50)

# delete the milk
d1.pop("milk",' milk not found')
print(d1)
print('=' * 50)


# print all iems
d4 = d1.items()
print(d4)
print('=' * 50)

