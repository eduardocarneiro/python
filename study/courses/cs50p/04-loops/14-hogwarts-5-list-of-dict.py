#!/usr/bin/env python3

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Stytherin", "patronus": None}
]

# will print the list of dictonary  
for student in students:
    print(student)
print(" ")

# will print all value of the list dict
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")