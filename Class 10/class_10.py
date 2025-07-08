courses = ("english", "urdu", "science") # tuple: course should not be modified
students = [] # empty list
cities = set() # empty set

for i in range(3): # 0 1 2
    print (f"\nStudent no. {i+1}" ) # Student no. 1
    name = input("write name of the student ") # name: ali
    course = input(f"Please select your course {"/".join(courses)}") # course: urdu
    city = input("Write name of your city: ") # city: Quetta

    if course not in courses: # if urdu is not in english, urdu, science
        print("Wrong course selected") # wrong course selected
         # existing loop skip start from next loop

    print("loop running here")
    student = { # Dictionary
        "name" : name, # "name" : ali
        "course": course, # "course" : urdu
        "city": city # "city" : quetta
    }

    students.append(student) # [{"name": ali, "course": urdu, "city": quetta }]
    cities.add(city) # { quetta }

print("Student detail: ") # Student detail
print(f"Total unique cities: {len(cities)}") # 1

for student in students: # 1
    print(f"Student name: {student["name"]}, city {student["city"]}, course {student["course"]}")
# Student name: ali, city: quetta, course: urdu

# List
# Tuple
# set
# Dictionary
# f-string
# .join function