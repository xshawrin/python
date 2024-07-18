class car:
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color
        
x = car('volvo', 2011, 'red')
print('brand is' , x.name)
print('model is', x.year)        
print('available color', x.color) 
      
