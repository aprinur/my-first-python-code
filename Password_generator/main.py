from util import random_pass

while True:
    amount = int(input('Input the length of password you want to create: '))
    print(f'Your password is {random_pass(amount)}')

    confirm = input('Continue generating password y/n : ')

    if confirm == 'n':
        break