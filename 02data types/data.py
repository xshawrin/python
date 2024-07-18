#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType
x = 4
print(type(x))

#convert from int to float, convert from float to int, convert from int to complex
#cannot convert complex numbers into another number type.
x = float(1)
y = int(1)
z = complex(1)
e = str(89)
print(x, y, z)
print(type(x))
print(type(y))
print(type(z))
print(type(e))

import random
value = random.randrange(1,9)
print(value)
Greetings = ['Hi', 'Hello','Hey', 'Hola']
x = random.choice(Greetings)
print(x, 'Shuchita')

