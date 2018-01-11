my_list = []
my_list.append(input('What will be the first item on the list?\n:'))
my_list.append(input('What will be the second item on the list?\n:'))
print(my_list)
index = input("Which list member would you like to change?\nType the number:\n1) " + my_list[0] + "\n2) " + my_list[1] + "\n:")
new_item = input('What should the second item be?\n:')
my_list[int(index) - 1] = new_item
print(my_list)
