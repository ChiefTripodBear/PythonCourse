my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99],
    'average': 'avg'
}
def average_grade(student):
    sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))

# create a new class
class Student:
    #dunder function, runs first. Self is an empty object
    def __init__(self, new_name, new_grade):
        #pass first arg as new_name, second as new_grade
        self.name = new_name
        self.grades = new_grade

    def average(self):
        return sum(self.grades) / len(self.grades)

#pass 'rolf smith' as 1st arg, becomes self.name, [] as 2nd arg, becomes self.grades
student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

print(student_one)
print(student_two)

print(student_one.average()) #because we're calling via an instance of the class, the method argument 'self' is automatically used
#print(Student.average()) #this will error because we're calling the class, not an instance of the class and not passing in the argument
print(Student.average(student_two)) #this is the same as line29



