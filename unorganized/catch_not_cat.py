cat_string = input('Please type "cat"\n:')

running = True

while running == True:
    if cat_string == 'cat':
        running = False
    else:
        cat_string = input('Please type "cat"\n:')
