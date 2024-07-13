#[] list = ordered, changable, duplicate ok.
#() tuple = ordered, unchangable, duplicate ok.
#{} set = unordered, unchangeable*, and unindexed. No duplicate members.


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

car = ["Audi", "BMW", "Kia", "Toyota", "Honda", "Kia"] # -6, -5, -4, -3, -2, -1
print(car)
print(len(car))

#for car in car:
  #  print(car)
   

print(type(car)) 
print(car[-1])
print("car[3:5]: ", car[3:5]) # first ignore, last include
print("car[-5:-2]", car[-5:-2]) # first include, last ignore
print(car[2:])
print(car[::2])# every second
car[3] = 'zeep'
car.append('volvo')# to add
car.insert(0, 'volvo')
car.sort()
print(car)
print(car.index('zeep'))
print(car.count('volvo'))

car = {"Audi", "BMW", "Kia", "Toyota", "Honda", "Kia"}
print(car)


