'''Object Oriented Programming'''

# class Car:
#     def __init__(self, model, manufacturer, color, top_speed):
#         self.model = model
#         self.manufacturer = manufacturer
#         self.color = color
#         self.top_speed = top_speed
#         self.speed = 0
    
#     def accelerate(self, amount):
#         self.speed += amount
#         if self.speed > self.top_speed:
#             self.speed = self.top_speed
            
#     def brake(self, amount):
#         self.speed -= amount
#         if self.speed < 0:
#             self.speed = 0
            
#     def get_speed(self):
#         return self.speed
    

# class Car:
#     color = 'red'
    
#     def drive(self):
#         print('brrrr')
        
# my_car = Car()
# print(f'type of my_car : {type(my_car)}')
# print(f'dir of my_car{dir(my_car)}')
# print(f'my_car : {my_car}')

# class Car:
#     def __init__(self, color:str, model:str, top_speed:int):
#         '''this is the car model'''
#         self.model = model
#         self.color = color
#         self.top_speed = top_speed
#         self.speed = 0
            
#     def accelerate(self, amount):
#         self.speed += amount
#         if self.speed > self.top_speed:
#             self.speed = self.top_speed

#     def brake(self, amount):
#         self.speed -= amount
#         if self.speed < 0:
#             self.speed = 0
    
#     def get_speed(self):
#         return self.speed
        
# car = Car('blue', '자동차' , 100)

# def get_speed(self, unit='mph'):
#     if unit == 'mph':
#         return self.speed
#     elif unit =='kmh':
#         return round(self.speed*1.60934, 2)
#     else:
#         raise ValueError('Invalid unit')


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def speak(self):
#         print('The animal speaks.')

# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed
        
#     def speak(self):
#         print('Woof!')
        
# class Cat(Animal):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
        
#     def speak(self):
#         print("Meow!")


# class Animal():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def speak(self):
#         print('speak')
        
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
        
#     def speak(self):
#         print("Meow!")
        
# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
    
#     def speak(self):
#         print("Wolf!")
        
        
# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14*self.radius**2
    
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side**2
    
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         return self.length*self.width
    
    
    
class Shape():
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14*self.radius**2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def get_area(self):
        return self.length*self.width