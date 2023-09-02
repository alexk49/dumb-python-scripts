# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

example = [1,2,3,4,5,6,7]

from random import shuffle

shuffle(example)

example


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


result = shuffle_list(example)

result

mylist = [' ', 'O', ' ']

shuffle_list(mylist)


def player_guess():
    guess=''
    while guess not in ['0','1','2']:    
        guess = input("Pick a number: 0,1, or 2")
    return int(guess)


player_guess()

myindex = player_guess()

myindex


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)


# initial list
mylist = [' ','O',' ']
# shuffle list 
mixedup_list = shuffle_list(mylist)
# user guess 
guess = player_guess()
# check guess 
check_guess(mixedup_list,guess)


