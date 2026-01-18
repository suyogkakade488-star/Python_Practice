'''create an empty dictionary allow 4 friends to enter their fav lang. as value & use key as their name
Assume that names are unique'''
# create empty dictionary
fav_lang = {}

# take input from 4 friends
for i in range(4):
    name = input("Enter your name: ")
    lang = input("Enter your favourite language: ")
    fav_lang[name] = lang

# print dictionary
print("Favourite languages of friends:")
print(fav_lang)
