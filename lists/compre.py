car = ["Audi", "BMW", "Kia", "Toyota", "Honda", "Kia"]
new_car = []
for x in car:
 if 'd' in x:
    new_car.append(x)
print(new_car)

print('-----')

new_car = [x for x in car if 'd' in x]
print(new_car)

print('-----')

new_car = [x for x in car if x != 'Kia']
print(new_car)

print('-----')

num = [ x for x in range(15) if x < 8]
print(num)

print('-----')

new_car = [x.upper() for x in car]
print(new_car)
new_car = ['Nissan' for x in car] #Set all values in the new list to 'Nissan'
print(new_car)

print('-----')
new_car = [x if x != 'Kia' else 'Nissan' for x in car]# Return "Nissan" instead of "Kia"
print(new_car)

