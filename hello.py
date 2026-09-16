print("Hello, World!")

if 5 > 2:
    print("five is greater than two")

x = 5
y = "Hello World!"

#Comments

print("I'm", 22, "years old")

"""
More comments
More comments
"""

x = str(3) #x string
y = int(3) #y integer
z = float(3) #z floater 3.0

print(type(x)) #for get the data type

#unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = fruits
y = fruits
z = fruits
print(x)
print(y)
print(z)
 
#Ouput variables
x = "Python"
y = "is"
z = "Amazing"
print(x + y + z)
print(x, y, z)

#Global variables
x = "awesome"

def myfunc():
    print("python is", x)

myfunc()

#global word
#gobal word is used for local variable to become global variable

def myfunc1():
    global x
    x = "fantastic"

myfunc1()
print("python is" + x)

