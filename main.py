from random import randint
user_name = input('Enter username ')
print('Welcome to the higher/lower game,' + user_name)
lower_bound = int(input('Enter the lower bound:'))
upper_bound = int(input('Enter the upper bound:'))

while lower_bound >= upper_bound:
    print('The lower bound must be less than the upper bound.')
    lower_bound = int(input('Enter the lower bound:'))
    upper_bound = int(input('Enter the upper bound:'))

random_num = randint(lower_bound, upper_bound)

guessed_num = int(input('guess '))

while True:
    if guessed_num > random_num:
        print('Too high ', end = '')
        guessed_num = int(input('guess again '))
    elif guessed_num < random_num:
        print('Too low, ', end = '')
        guessed_num = int(input('guess again '))
    elif guessed_num == random_num:
        print('You won,' + user_name)
        break
