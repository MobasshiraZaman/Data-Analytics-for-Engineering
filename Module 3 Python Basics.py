# Module 3 Python Basics
# ISYE 570
# Mobasshira Zaman

print("Welcome to ISYE 570")
print("My name is Mobasshira Zaman")


# Module 3: 3.3 video
# Write comments with hash sign.

#Example of String
#Indices begins at 0
myName = 'Mobasshira Zaman'
print(myName[0])
print (myName[5])

print ('The letter in the 0th position is '+ myName[0])
print ('The letter in the 9th position is '+ myName[11])

introString= 'My name is: '
print(introString+myName)

#Module 3: 3-4 video
# Examples of lists
myList = [9, 'dog', 1.8, 3.0, True, 9.2, False, 'ISYE']
print(myList)
print(myList[0])
print('The first item in the list is:', myList[0])
print("Second item is:", myList[1])
print('Three items are:', myList[0], myList[1], myList[4])

# Examples of Dictionary objects
myHouse = {
    'door': 'white',
    'fence': 'black',
    'living room': 'beige',
    'kitchen': 'grey'
}

print(myHouse)
print("The colour of my door is:", myHouse['door'])
test = {
    0: 'first position',
    1: 'second position'
}

myFavorites = {
    'colors': ['pink', 'black'],
    'animals': ['dog', 'cat'],
    'numbers': [13, 21, 97, 100]
}
print('My favorite colors are', myFavorites['colors'])
print('My absolute favorite color is', myFavorites['colors'][0])
fav_colors = myFavorites['colors']
print(fav_colors)

print('My favorite favorite color is', fav_colors[0])

