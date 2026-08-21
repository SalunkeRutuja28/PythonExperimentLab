students = ["Hermoine","Harry","Ron"] #List

# print(students[0])
# print(students[1])
# print(students[2])

for student in students:
    print(student)

for i in range(len(students)):
    print(i+1, students[i])

#dictionary dict
members = {"Hermione": "Gryffindor", "Ron": "Gryffindor", "Harry": "Gryffindor", "Draco": "Slytherin"}

# print(members["Hermione"])
# print(members["Harry"])
# print(members["Ron"])
# print(members["Draco"])

for member in members:
    print(member, members[member], sep=",")

#list of dictionaries

hstudents = [
    {"name": "Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name": "Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name": "Draco", "house":"Slytherin", "patronus": None}
]

for hstudent in hstudents:
    print(hstudent["name"], hstudent["house"], hstudent["patronus"], sep=",")