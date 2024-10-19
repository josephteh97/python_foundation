# 1. lists
# Create a list
fruits = ["apple", "banana", "cherry"]

# Access elements
print(fruits[0])  # Output: apple

# Modify elements
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# Add elements
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']


# 2. For Loops
# Loop through a list
fruits = ["apple", "orange", "cherry", "grape"]

for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)



# 3. While Loops
count = 0

while count < 5:
    print("Count is:", count)
    count += 1  # increment the counter


# 4. Functions
# Define a function
def greet(name):
    print("Hello, " + name + "!")

# Call the function
greet("Alice")

def add(a, b):
    return a + b

result = add(3, 5)
print("Sum:", result)  # Output: Sum: 8


# 5. Importing Modules
import math

# Use functions from the math module
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793


from math import sqrt

print(sqrt(25))  # Output: 5.0

