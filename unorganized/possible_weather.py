import random
response = input('Would you like to know the weather?\n:')

possible_weather = ['Foggy', 'Sunny', 'Rainy', 'Smokey', 'Cloudy']

if response == 'yes':
    print("Looks like it's" + random.choice(possible_weather) + 'outside')
