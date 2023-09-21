#!/usr/bin/env python3

#students = ["Hermione", "Harry", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
 }

# print everything as a dict
print(students)
print(" ")

# print the value
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
print(" ")

# will print the key
for student in students:
    print(student)
print(" ")

# will print the value
for student in students:
    print(student, students[student], sep=" - ")