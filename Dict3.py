User = {"Name": "Suyog","Surname": "Kakade","City": "Nagar","Age": 30}
del User["City"] #Removing a specific item by key del

# User = {"Name": "Suyog","Surname": "Kakade","Age": 30}
remove_age = User.pop("Age")

#User = {"Name": "Suyog","Surname": "Kakade",}
print(remove_age)

#removing a last inserted items only in  python 3.7+
User.popitem()
print(User)
