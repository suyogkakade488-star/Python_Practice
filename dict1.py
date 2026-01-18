# Empty dictionary
ed = {}
print("ed :", ed)
print("Type of ed :", type(ed))
print()

# Dictionary with INT keys
students = {
    1: 25,
    2: 26,
    3: 22,
    4: 21
}
print("students :", students)
print()

# Dictionary with STRING keys
user = {
    "Name": "Suyog",
    "Surname": "Kakade",
    "City": "Nagar",
    "Age": 30
}
print("user :", user)
print()

# Mixed dictionary (int, string, tuple keys)
mix = {
    "ID": 42,
     "Roll No":99,
    ("X", "Y"): [10, 20]
}
print("mix :", mix)
print()

# Accessing values
print("User Name :", user["Name"])
print("Student Roll number:", mix["Roll No"])
print("Student age:", user["Age"])
print("Tuple key value :", mix[("X", "Y")])
