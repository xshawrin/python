def mylist():
 x = "python"
 y = "is"
 z = "awsome"
 print(x , y , z)
mylist() 
print("------")#if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def mylist(colors, cars):
  print(colors+ " " + cars)
mylist("red", "audi")
mylist("blue", "toyota")
mylist("black", "nissan")

def list(*cars):#If the number of arguments is unknown, add a *
 print('The selected car is' + ' ' + cars[2])
list('audi', 'toyota', 'kia') 
print("------")#also send arguments with the key = value syntax
def list(cars1, cars2, cars3):
 print('My favorite car is' + " " + cars2)
list(cars1 = 'kia', cars2= 'audi', cars3= 'toyota') 

def mylist(cars = 'Audi'):#If we call the function without argument, it uses the default value:
 print('My favorite car is' + " " + cars)
 mylist('Toyota')
 mylist()
 mylist('kia')
 print('-----')
def num(x):
 return 9 * x
print(num(3))
print(num(5))
print(num(2))


print('-----')


def birthday(name, age):
 print(f'Happy birthday to you {name}.')
 print(f'you are {age} years old.')
birthday('shuchita', 31)

print('-----')

def add(x, y):
 z = x + y
 return(z)
def substract(x, y):
 z = x - y
 return(z)
def multiply(x, y):
 z = x * y
 return(z)
print(add(2,3))
print(multiply(2,3))
print(substract(2,3))