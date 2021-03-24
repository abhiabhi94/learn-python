import random

MY_NUM = random.randrange(1, 100)

print('Let us play a guessing game.\n You have to guess a number between 1 and 100')


while(True):
    num = int(input('Enter a number between 1 and 100:\t'))
    if num == MY_NUM:
        print('Yeah!, You guessed it right.')
        break
    elif num > MY_NUM:
        print('Your nunber guessed is larger than the actual number. Please try again\n')
    else:
        print('Your nunber guessed is smaller than the actual number. Please try again\n')
