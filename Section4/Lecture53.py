class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

matrix = Movie('The Matrix', 1994)
print(matrix.name)

class Student:
    def __init__(self, name):
        self.name = name

movies = ['Matrix', 'Finding Nemo']
print(movies.__class__)

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}>'

    def __str__(self):
        return f'Garage with {len(self)} cars.'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(len(ford))

print(ford[0]) #Garage.__getitem__(Ford, 0)

print(ford)
