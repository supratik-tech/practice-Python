


student = {
    "name": "Supratik",
    "age": "19",
    "subject": {                # nested dictionary
        "Chemistry" : "94",
        "English" : "90",
    }
}
# }
print(student.update({"Favourite Subject" : "Programming"}))
print(student["subject"]["Chemistry"])
print(student.keys())
print(len(student))
print(list(student.keys()))
print("values of students:",student.values())
print("list of values:",list(student.values()))
print("List of keys:",list(student.keys()))
print("Length of values ",len(student.values()))
pairs = list(student.items())
print("1st item:",pairs[0])
print(student["name"]) # Supratik is printed
print(student.get("name2")) # None is returned if the key is not found
print(student.get("Favourite Subject"))
 # KeyError is raised if the key is not found