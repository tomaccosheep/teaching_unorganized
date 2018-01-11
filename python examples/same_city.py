import random
city_list = ['seattle', 'portland', 'salem']
user_choice = input('What is your favorite city? ')
computer_choice = random.choice(my_list)
if computer_choice == user_choice:
    print('Correct!')
else:
    print('Incorrect!')
