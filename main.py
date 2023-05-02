from pprint import pprint

players = [
    {'name': 'James', 'age': 22},
    {'name': 'Mark', 'age': 25},
    {'name': 'Carl', 'age': 17},
    {'name': 'Jonh', 'age': 34},
    {'name': 'Michael', 'age': 15},
    {'name': 'Carlos', 'age': 12},
    {'name': 'Tom', 'age': 46},
    {'name': 'King', 'age': 36}
]


for p in players:
    name = p['name']
    age = p['age']
    print(name, age)