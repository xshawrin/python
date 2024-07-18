#() tuple = ordered, unchangable, duplicate ok.
#String, int and boolean data types:
car = ("Audi", "BMW", "kia", "Toyota", "honda", "Kia")
print(len(car))
car = ("Audi", "BMW", "kia", "Toyota", "honda", "Kia")
num = (3, 4, 5, 6)
bool = (True, False, True)
print(type(car))

#Using the tuple() method to make a tuple
num = tuple((3, 4, 5, 6, 7))
#print(car[-1])
#print("car[3:5]: ", car[3:5]) # first ignore, last include
#print("car[-5:-2]", car[-5:-2]) # first include, last ignore
#print(car[2:])
#print(car[::2])# every second
if 'Audi' in car:
    print('yes, its present')
print('----a')    
x = list(num)
x[1] = 8
num = tuple(x)
print(num)

print('----b')    

x = list(num)
x.append(9)
num = tuple(x)
print(num)

print('----c')

x = list(num)
x.remove(3)
num = tuple(x)
print(num)

print('----d')

x = list(num)
x.insert(0, 1)
num = tuple(x)
print(num) 

print('----e') 

x = (2,)#Create a new tuple with the value and add the value
num += x
print(num)

print('----f') 
(red, blue, black, *white) = car
print(red)
print(red)
print(black)
print(white)

print('----') 

x = car + num #to join
pass

x = car * 2
print(x)
x = car.count('kia') 
pass
x = car.index('Toyota')
pass


