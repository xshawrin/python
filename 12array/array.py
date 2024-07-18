#array is container that holds multiple value of the same type
#An array can hold many values under a single name, and you can access the values by referring to an index number.
#how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.
car = ["Audi", "BMW", "Kia", "Toyota", "Honda", "Kia"]
#print(car[-1])
#print("car[3:5]: ", car[3:5]) # first ignore, last include
#print("car[-5:-2]", car[-5:-2]) # first include, last ignore
#print(car[2:])
#print(car[::2])# every second
car[3] = 'zeep'
#print(car)
car.append('volvo')# to add
car.insert(0, 'volvo')
#print(car)
#print(car.index('zeep'))
#print(car.count('volvo'))
car.remove('Kia')
x = len(car)
for x in car:
    pass