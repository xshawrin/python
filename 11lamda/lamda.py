#A small anonymous function, 
#lamda parameter :expression
car = lambda x : x * 3
add = lambda a, b : a + b
print(add(3, 5))
value = lambda x, y: x if x > y else y
print(value(5, 6))
value = lambda x, y: x if x < y else y
print(value(4, 7))
ful_name = lambda fname, lname: fname + ' ' + lname
print(ful_name('shuchita', 'shawrin'))
even = lambda x: x % 2 == 0
print(even(5))
age = lambda x: True if x > 18 else False
print(age(22))