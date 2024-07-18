#{} set = unordered, unchangeable*, and unindexed. No duplicate members.
#Sets cannot have two items with the same value.
car = {"Audi", "BMW", "Kia", "Toyota", "Honda", "Kia", True, 1, 2, 0, False}
num = {3, 4, 5, 6}
num_ =[10, 11, 12, 15]
#False and 0 is considered the same value:
#True and 1 is considered the same value:
#Set items can be of any data type:
#cannot access items in a set by referring to an index or a key.
print(car)
print(len(car))
print(type(car))
print('Honda' in car)
print('Honda' not in car)
car.update(num)
pass
car.update(num_)
car.remove(False)
car.discard(15)
pass
x = car.pop()
print(x)
print(car)
pass
