
print(" STRINGS AND CHARACTERS ")
# str1 = input("enter a string = ")
str1 = "Python is the king of AI"
str2 = " JA ,JA .TUR, JA,ja "

# print(str1[0])
# print(str1[1])
# print(str1[-1])

# for i in str1:
#     print(i)
    
print("OPERATIONS IN Python")

print("LENGHT OF str1= ",len(str1))

print(" index same hi h ")

sli = str1[1:10:1]
print("Slicing of str1= ",sli)

print("Concatination of str1 + str2=  ",str1+str2)

print("Checking membership ", "king" in str1)
print("checking membership  ", 'king' not in str1)

print(" methods in strings")
print("uppercase ",str1.upper())
print("lowercase ",str1.lower())
print("capitalize ",str1.capitalize())
print("title ",str1.title())
print("swapcase ",str1.swapcase())
print("finding some char or word ",str1.find("king"))

print("replace ",str1.replace("king",'foundation'))

str_split = str2.split(",")
print("split ",str_split)

j= ','.join(str_split)
print("split to join== ",j)


print("checking methods")
print("startswith p =", str1.startswith("p"))
print("endswith p=", str1.endswith("p"))
print("isalpha=", str1.isalpha())
print("isdigit=", str1.isdigit())
print("isalnum=", str1.isalnum())






