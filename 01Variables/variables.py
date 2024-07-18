abcEfg = 10 # Camel Case
abc_efg = 10 # snake Case

print(abcEfg)
print(abc_efg)
helloWorld =34
Hello_worldSweden = 34

print('----')
x, y, z = "orange", "banana", "apple"
print(x)
print(y)
print(z)

x= y= z = "orange"
print(x)
print(y)
print(z)

fruits = ["orange", "banana", "apple"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "python is awsome"
print(x)

x = "python"
y = "is"
z = "awsome"
print(x, y, z)

x = "python "
y = "is "
z = "awsome"
print(x+ y+ z)

#string and a number with the + operator, Python will give an error
# to separate them with commas, which even support different data types
x = "key"
y = "6"
print(x, y)

x = " Sweden"
def myfun():
    x = " Bangladesh"
    print('I live in'+ x)

myfun()
print('I live in'+ x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = " Sweden"
def myfun():
    global x
    x = " Bangladesh"
    print('I live in'+ x)

myfun()
print('I live in'+ x)


