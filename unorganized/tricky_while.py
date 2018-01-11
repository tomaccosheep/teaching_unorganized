import os
os.system('clear')
running = True
favorite_fruit = 'apple'
favorite_sport = 'soccer'
favorite_food = 'pizza'

while running == True:
    if favorite_fruit == 'orange':
        favorite_sport = input("What is your favorite sport?\n")
    if favorite_sport == 'soccer':
        favorite_food = input("What is your favorite food?\n")
    if favorite_food == 'nachos':
        favorite_fruit = input("What is your favorite fruit?\n")
    if favorite_sport == 'football':
        running = False
