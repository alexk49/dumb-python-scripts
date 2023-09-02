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

3 % 2

2 % 2

41 % 40

20 % 2

21 % 2 == 0


def even_check(number):
    return number % 2 == 0


even_check(20)

even_check(21)

even_check(30)


# +
# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST
# -

def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass 
        
    return False


check_even_list([1,2,3,4,5])

check_even_list([1,3,5,7])


def check_even_list(num_list):
    #return all even numbers in a list 
    #placeholder variables
    even_numbers = []
    
    
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass 
        
