import random
human_favorite_country = input('What is your favorite country? ')
country_list = ['USA', 'CAR', 'CHAD', 'CAMEROON', 'FRANCE']
favorite = random.choice(country_list)
second_favorite = random.choice(country_list)
while favorite == second_favorite:
    second_favorite = random.choice(country_list)

if human_favorite_country == favorite:
    print("That's my favorite, too!")
else:
    if human_favorite_country == second_favorite:
        print("Okay, that's my second favorite.")
    else:
        print("I don't like that country.")
print(favorite, second_favorite)
