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

# Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left of

# Allows you create a sequence of values over time.
#
# The main difference in syntax is the use of a "yield statement"

# When a generator function is compiled they become an object that supports an iteration protocol
# That means when they are called in your code they don't actually return a value then exit

# Generator functions will automatically suspend and resume their execution and state around the last point of value generation
#
# the advantage is that instead of having to compute an entire series of values up from the generator computes one value waits until the next value is called for

# For example, the range() function doesn't produce a list in memory for all the values from start to stop
#
# Instead it just keeps track of the last number and the step size to provide a flow of numbers

# range itself is a generator, which is why you have to assign it to a list manually eg. list(range(0,10))

def create_cubes(n):
    #create empty list
    result = []
    # iterate through, numbers is variable assigned to function
    for x in range(n):
        # append the list, once action performed
        result.append(x**3)
    # return the newly created list, which is all kept in memory
    return result


create_cubes(10)

for x in create_cubes(10):
    print(x)


# only needed one value at a time in memory to get to the next number

def create_cubes_with_yield(n):
    
    for x in range(n):
        yield x**3


# +
create_cubes_with_yield(10)

# don't see list, as this is just to generator 
# -

for x in create_cubes_with_yield(10):
    print(x)


# this is much more memory efficient ^ 

def gen_fibon(n):
    
    a = 0
    b = 1
    
    for i in range(n):
        yield a
        # reset a to be equal to b 
        # rest b to be equal to sum of previous a+b 
        a,b = b,a+b


for number in gen_fibon(10):
    print(number)


def gen_fibon_as_normal_func(n):
    
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output


gen_fibon_as_normal_func(10)

for number in gen_fibon_as_normal_func(10):
    print(number)



def simple_gen():
    for x in range(3):
        yield x


for x in simple_gen():
    print (x)

g = simple_gen()

g

print(next(g))

print(next(g))

print(next(g))

print(next(g))

s = 'hello'

for letter in s:
    print(letter)

s_iter = iter(s)

next(s_iter)

next(s_iter)

next(s_iter)

next(s_iter)

next(s_iter)

next(s_iter)
