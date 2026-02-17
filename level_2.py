#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
marks = {}
A = int(input("Enter marks of Math = "))
marks.update({"Math" : A})
B = int(input("Enter marks of Physics = "))
marks.update({"Physics" : B})
C = int(input("Enter marks of chemistry = "))
marks.update({"Chemistry" : C})
D = int(input("Enter marks of Biology = "))
marks.update({"Biology" : D})

print(marks)
