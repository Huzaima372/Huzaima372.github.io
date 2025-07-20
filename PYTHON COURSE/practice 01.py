# -------------------------------
#  Question 1: Age Calculator
# -------------------------------
# Description:
# Ask the user for their birth year and calculate their age.
# Assume the current year is 2025.

birth_year = int(input("Enter your birth year: "))
real_age = 2025 - birth_year
print("You are", real_age, "years old.")

print("-" * 40)  # Just a line separator

# -------------------------------
#  Question 2: Bus Fare Checker
# -------------------------------
# Description:
# Ask the user for their age and print ticket fare based on age:
# - Age <= 5: Free
# - 6 to 18: ₹100
# - 19 to 60: ₹200
# - > 60: ₹70

age = int(input("Enter your age: "))

if age <= 5:
    print("Free")
elif age <= 18:
    print("Fare is ₹100")
elif age <= 60:
    print("Fare is ₹200")
else:
    print("Fare is ₹70")

print("-" * 40)

# -------------------------------
# Question 3: Palindrome Checker
# -------------------------------
# Description:
# Ask the user to enter a word and check if it's a palindrome.
# A palindrome is a word that reads the same backward.

word = input("Enter a word: ")

reversed_word = word[::-1]

if word == reversed_word:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
