car = ["Audi", "BMW", "kia", "Toyota", "honda", "Kia"]
car.sort()
car.sort(reverse = True)
print(car)

print('-----')

def num(a):#The function will return a number that will be used to sort the list (the lowest number first)
  return abs(a - 25)#what abs? is it possible with string?
new_num = [20, 19, 23, 30, 38, 31, 15, 10, 3,]
new_num.sort(key = num)
print(new_num)

print('-----')
car.sort(key = str.lower)
print(car)

# want to reverse the order of a list, regardless of the alphabe
car.reverse()
pass
