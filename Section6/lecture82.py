import json

file = open('Section6/data/friends_json.txt', 'r')
file_contents = json.load(file) #reads file and turns it into a dictionary
file.close()

print(file_contents['friends'][0])

#you can write a json file by creating a dictionary like below
cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

#create a file in write mode called cars_json.txt, use json.dump to drop the dictionary in the file and close it
file = open('Section6/data/cars_json.txt', 'w')
json.dump(cars, file)
file.close()