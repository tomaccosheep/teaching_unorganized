import random
list1 = ['0', '1', '2']
list2 = ['3', '4', '5']
list3 = ['6', '7', '8']

big_list = [list1, list2, list3]

print(random.choice(big_list[0]) + random.choice(big_list[1]) + random.choice(big_list[2]))

many_numbers = ''
for i in big_list:
    many_numbers += random.choice(i)
print(many_numbers)
