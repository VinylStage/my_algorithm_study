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
    

class Car:
    color = 'red'
    
    def drive(self):
        print('brrrr')
        
my_car = Car()
print(f'type of my_car : {type(my_car)}')
print(f'dir of my_car{dir(my_car)}')
print(f'my_car : {my_car}')