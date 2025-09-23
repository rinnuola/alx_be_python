#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("Ade Anna")


# In[2]:


print(3+5)


# In[3]:


print(2*2*2)


# In[6]:


def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")
greet("Anna")


# In[12]:


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(5, 3)  # call the function here
print(result)



# In[13]:


def greet(name="Guest"):
    """Greets a person, defaults to Guest if no name is given."""
    print(f"Hello, {name}!")
    
greet("Ade")
greet()


# In[14]:


def introduce(name, age):
    """Introduces a person with their name and age."""
    print(f"My name is {name} and I am {age} years old.")

introduce("Anna", 25)


# # Basic Lambda Function

# In[15]:


add = lambda x, y: x + y
result = add(5, 3)
print(result)


# # Lambda with No Parameters

# In[16]:


say_hello = lambda: "Hello!"
print(say_hello())


# # Function Parameters and Return Values

# In[23]:


def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area

# Passing argument
calculate_area(10, 5)  


# # Positional Parameters
# 
# Arguments are matched based on their position.

# In[24]:


def greet(first, last):
    print(f"Hello, {first} {last}!")

greet("Ade", "Anna")  


# # Keyword Parameters
# 
# Arguments are passed with the parameter name.

# In[25]:


def user_info(name, age=None):
    """Prints user information."""
    print(f"Name: {name}")
    if age:
        print(f"Age: {age}")

user_info(name="Bob", age=30)


# # Default Parameters
# 
# Parameters can have a default value.

# In[27]:


def greet(name="World"):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

greet()        
greet("Anna") 


# # Variable-length Parameters
# 
# Use *args for multiple positional arguments.
# 
# Use **kwargs for multiple keyword arguments.

# In[28]:


def add_numbers(*args):
    return sum(args)

print(add_numbers(2, 3, 5))  

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Anna", age=25, country="Nigeria")


# # Return Values
# 
# Functions can send back results using return.
# They can return single or multiple values.

# In[29]:


def square(number):
    """Returns the square of a number."""
    return number * number

squared_value = square(4)
print(squared_value)  


# # Returning multiple values:

# In[31]:


def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([3, 7, 1, 9])
print(low, high)  


# # Variable Scope and Functions
# Local vs Global Scope
# 
# Local variable → defined inside a function, only accessible there.
# 
# Global variable → defined outside functions, accessible everywhere.

# In[32]:


count = 0  # Global variable

def increment():
    count = 0  # Local variable (different from global)
    count += 1
    print("Inside function:", count)

increment()
print("Outside function:", count)


# # global Keyword
# 
# Used to modify a global variable inside a function.

# In[33]:


count = 0

def increment_global():
    global count
    count += 1

increment_global()
print(count)  


# # nonlocal Keyword
# 
# Used to modify a variable from an enclosing (outer) function inside a nested function.

# In[34]:


def outer_function():
    x = 10  # Enclosing function variable

    def inner_function():
        nonlocal x
        x += 5  # Modify outer variable

    inner_function()
    print("Modified value of x:", x)

outer_function()


# # Practice Exercises
# Exercise 1: Write a function to greet the user by name.
# 
# Instructions:
# 
# Define a function called that takes one parameter, (name).
# Inside the function, create a greeting message that includes the name passed as an argument.
# Print the greeting message using the print function.

# In[37]:


def greet_user(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")

# Test
greet_user("Anna")   
greet_user("Ade")    


# # Exercise 2: Create a function to calculate the area of a rectangle.
# 
# Instructions:
# 
# Define a function that takes two parameters, length and width.
# Inside the function, multiply the length and width to calculate the area.
# Use the return statement to return the calculated area.

# In[40]:


def rectangle_area(length, width):
    """Calculate the area of the rectangle"""
    return length * width
#Test
area = rectangle_area(10, 5)
print(f"The area of the rectangle is {area}")


# # Exercise 3: Develop a function to check if a number is even or odd.
# 
# Instructions:
# 
# Define a function that takes one parameter, number.
# Inside the function,check the remainder after dividing the number by 2 is equal to zero.
# If the remainder is zero, the number is even. Print a message indicating the number is even.
# If the remainder is not zero, the number is odd. Print a message indicating the number is odd.

# In[42]:


def check_number(number):
    """Checks if a number is even or odd."""
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# Test
check_number(10)  
check_number(7)   


# In[ ]:




