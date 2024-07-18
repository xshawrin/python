#{}  items are ordered, changeable, and do not allow duplicates..
#String, int, boolean, and list data types
#Using the dict() method to make a dictionary
car = {
    'Brand': 'Audi',
    'model': 'F5',
    'year' : 2014,
    'year': 2020, #changable
    "colors": ["red", "white", "blue"]
}
print(car)
print(len(car))
print(type(car))
item = dict( color ='red', year = 2021, model = 'sun')
print(item)
#can access the items of a dictionary by referring to its key name, inside square bracket
x = car['model']
#called get() that will give you the same result
x = car.get('model')
pass
print('----')
x = car.keys()
print(x)
print('----')
x = car.values()
print(x)
print('----')
x = car.items()
print(x)
car['year'] = 2022
print(x)

print('----')#to add, copy and check if present
if 'model' in car:
    pass
car.update({'colors': 'black'})#change as well
car['launch'] = 2022
pass
new = car.copy()#.dict() works same
pass

print('----')#for loop
for x in car:
 #print(car[x])
 pass 
for x in car. values():
 pass
for x in car.keys():
 pass
for x, y in car.items():
  pass

print('----') #to remove: pop(), del, popitem(),clear()
car.pop('model')
pass

del car['year']
pass

print('----') #nested
car = {
 'Audi':{
    'model': 'F5',
    'year' : 2014,
    'colors': 'red'
 },
'kia':{
    'model': 'ev9',
    'year' : 2018,
    'colors': 'red'

 },
'Toyota': {
'moodel': 'corolla',
'year': 2014,
'color': 'blue'
 }
}

#or
Audi = {
 'model': 'F5',
 'year' : 2014,
 'colors': 'red'
}
kia = {
    'model': 'ev9',
    'year' : 2018,
    'colors': 'red'

}
Toyota ={
'moodel': 'corolla',
'year': 2014,
'color': 'blue'
 }
cars = {
  'Audi' : Audi,
  'kia': kia,
  'Toyota' : Toyota
}
print(cars)

for x, obj in car.items():
  print(x)
  for y in obj:
    print(y, '=', obj[y])# need to understand logic

print('--------Practice---------')
