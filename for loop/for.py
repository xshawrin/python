#A for loop is used for iterating over a sequence

car = ["Audi", "BMW", "Kia", "Toyota", "Honda", "Kia" 'Nissan']
for x in car:
    if x == 'Toyota':
        print('found')
        continue
    print(x)

print('-----')
for z in range(1,11):
    print(z)

print('-----')
#it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(1,22,3):
 print(x) 

print('-----')

for x in range(6):
 print(x)
else:
 print('finished')

print('-----')
#Break the loop when x is 3, and see what happens with the else block
for x in range(6):
 if x == 5: break
 print(x)
else:
 print('finished')

print('-----')

car = [1,2,3]
vehicle = ["Toyota", "Honda", "Kia"]
for x in car:
  for y in vehicle:
    print(x,y)