number_list =  [1, 2, 5, 3, 5]
mistake = False
biggest_recent = number_list[0]
for i in range(0, len(number_list) - 1):
    if number_list[i] > biggest_recent:
        biggest_recent = number_list[i]
    if biggest_recent >= number_list[i + 1]:
        if mistake == False:
            mistake = True
        else:
            print('False')
            #return False
            break
print('True')
#return True
