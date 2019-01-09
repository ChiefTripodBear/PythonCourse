#read csv
file = open('Section6/data/csv_data.txt', 'r')
lines = file.readlines()
file.close()

#strip newlines out of file
lines = [line.strip() for line in lines[1:]]

#split fields by comma, and save into set variables
for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()
    print(f'{name} is {age}, studying {degree} at {university}.')

#printing sample csv, can use this .join method to write data into a csv
sample_csv_value = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)