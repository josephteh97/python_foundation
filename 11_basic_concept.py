# 1. build python envrionment 
# To begin, you'll need Python installed on your machine. You can install it from Python's official website.
# Once installed, you can run Python scripts from your terminal or use an IDE like PyCharm, VSCode, or Jupyter Notebook

# 2. print
print("Hello, World!")


# 3. variable
# variables store data that you can use later in your prg
name = "Alice"  # string variable
age = 25        # integer variable
height = 5.5    # float variable

print("Name:", name)
print("Age:", age)
print("Height:", height)


# Input
user_name = input("What is your name?")
print("Hello," + user_name + "!")

# Conditional Statements
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif 13 <= age < 18:
    print("You are a teenager.")
else:
    print("You are a child.")

