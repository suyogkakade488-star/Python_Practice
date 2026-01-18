'''
Iterating through a dictionary
You can iterate through a dict in several ways
'''

grades = {
    "Maths": 90,
    "Science": 80,
    "History": 99
}

# 1️⃣ Iterating over KEYS (default)
print("Iterating over KEYS:")
for subject in grades:
    print(subject)

print()

# 2️⃣ Iterating over VALUES
print("Iterating over VALUES:")
for score in grades.values():
    print(f"Score is: {score}")

print()

# 3️⃣ Iterating over KEY–VALUE pairs
# items() returns a tuple (key, value)
print("Iterating over KEY-VALUE pairs:")
for subject, score in grades.items():
    print(f"The score for {subject} is {score}")
