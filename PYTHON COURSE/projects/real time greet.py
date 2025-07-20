# Create a Python program that displays the current time and greets the user based on the time of day.

import time

# Get current time
timestamp = time.strftime('%H:%M:%S')
print("Current time:", timestamp)

# Extract the hour and convert it to integer
hour = int(time.strftime('%H'))
print("Hour:", hour)

# Greet the user based on time
if 0 <= hour < 12:
    print("Good morning")
elif 12 <= hour < 18:
    print("Good afternoon")
elif 18 <= hour < 24:
    print("Good evening")
else:
    print("error h baaba")
