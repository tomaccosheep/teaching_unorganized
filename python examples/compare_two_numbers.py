def compare(number1, number2):
    if number1 == number2:
        return 'They are equal'
    elif number1 > number2:
        return '{} is greater than {}'.format(number1, number2)
    elif number1 < number2:
        return '{} is greater than {}'.format(number2, number1)

print('You imported compare_two_numbers.py')
