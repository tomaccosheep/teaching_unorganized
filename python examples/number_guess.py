#guess the numbers
number_list = ['0', '1']
while len(number_list) != 0:
    guess = input('number: ')
    if guess in number_list:
        number_list.remove(guess)
    print('answers: ' + str(number_list))
