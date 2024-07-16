a = '''my name is "Shuchita".
I live in Sweden.
life is Fun. I am'''
print(a)

print(len(a))
print(a[22:32]) # comments
print('----------')
def country():
 for a in 'Sweden':
  print(a)
country()
print('----------')

print('fun' in a)

if 'pain' in a:
 print('Yes, Horray')
else:
 print('No, Its not')

print(a.upper())
print(a.replace('m', 'k'))
print(a.split())
print(a.strip())



b = '33'
#To add a space between them, add a " " or ' '.
c = a + ' ' + b
print(c)

def age():
  b = 33
  a = f"my name is \"Shuchita\". \nI live in Sweden. \nlife is Fun. \nI am \"{b}\""
  print(a)
age()
e = a.capitalize()
print(e)

