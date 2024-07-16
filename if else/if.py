a = 66
b = 200
c = 66
if b > a:
    print('yes, b is greater than a')
    print('A') if a > b else print('B')
print('----')

a = 66
b = 55
c = 66
if b > a:
 print('yes, b is greater than a')
elif a == c:
 print('a and c is equal')
else:
  print('b is smaller than a')

print('----')

a = 66
b = 55
c = 66

if b > a:
 print('yes, b is greater than a')
elif a == c:
 print('a and c is equal')
else:
  print('b is smaller than a')

print('----')#Ternary Operators, or Conditional Expressions
print('A')if a < b else print('==') if a == c else print('B')

print('----')
if a and c > b :
  print( 'contion teue')
if a > b or b > c:
  print('one is true')
if not a > c:
  print('a is not greater')
if a > 20:
  print('above than 20')
  if a > 40:
    print( 'above also 40')
  else:
    print('not 40')