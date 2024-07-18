#[] list = ordered, changable, duplicate ok.


#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
#thislist = list(("apple", "banana", "cherry")) # note the double round-brackets, print(thislist)

car = ["Audi", "BMW", "Kia", "Toyota", "Honda", "Kia"] # -6, -5, -4, -3, -2, -1
#print(car)
#print(len(car))

#for car in car:
    #print(car)
   

#print(type(car)) 
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

#To append elements from another list to the current list, use the extend() method.
car = ["Audi", "BMW", "Kia"]
vehicle = ["Toyota", "Honda", "Kia"]
car.extend(vehicle)
car.remove('Kia')
print(car)
#'pop()' method removes the last item, 'pop(1)' remove second item
#The del keyword also removes the specified index. del keyword can also delete the list completely.
del car[1]
print(car)

new_car = vehicle.copy() # list() also use for copy
print(new_car)

print('----')


for x in car: #to join
    vehicle.append(x)
print(vehicle)

print('----')
car.extend(vehicle)#to join
print(car)