import random
import string
for i in range(3):
    print(random.choice(string.ascii_letters))

i = 0
while i < 10:
    print(i)
    i += 1

my_string = ''
for i in range(4):
    my_string += 'a'
print(my_string)


for i in range(4):
    print(i)

i = 0
while i < 4:
    print(i)
    i += 1

prob = int(input('What percent should be a, not b? '))
for i in range(10):
    if random.randint(0, 100) > prob:
        print('b')
    else:
        print('a')
