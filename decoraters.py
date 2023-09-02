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

# A decorator is a way of extending a function, wiwth an @ operator. This can be removed when if it is no longer needed. 
#
#     @some_decorator
#     def simple_func()
#         #do something
#         return something

def func():
    return 1


func()

func


def hello():
    return "Hello!"


greet = hello

greet()

hello()

del hello

hello()

greet()

# greet completely copies the hello function, and isn't just dependent on it





def hello(name="Jose"):
    print("The hello() function has  been executed!")
    
    def greet():
        return "\t This is the greet function inside hello"
    
    def welcome():
        return "\t This is welcome() inside hello"
    
    print(greet())
    print(welcome())


hello()

print("This is the end of the hello function!")

welcome()





def hello(name="Jose"):
    print("The hello() function has  been executed!")
    
    def greet():
        return "\t This is the greet function inside hello"
    
    def welcome():
        return "\t This is welcome() inside hello"
    
    print("I am going to return a function")
    
    if name == "Jose":
        return greet
    else:
        return welcome


my_new_func = hello("Jose")

my_new_func

print(my_new_func())


def cool():
    
    def super_cool():
        return "I am very cool"
    
    return super_cool


some_func = cool()

some_func

some_func()





def hello():
    return "Hi Jose!"


def other(some_def_func):
    print("Other code runs here")
    print(some_def_func())


hello

hello()

# the raw function of hello will be executed in other

other(hello)







def new_decorator(original_func):
    
    def wrap_func():
        
        print("Some extra code, before the original function")
        
        original_func()
        
        print('Some extra code, after the original function')
        
        return wrap_func


# takes in the original function, passes some code then passes the original function then passes more code. 
#
# original function has been "wrapped" up with the wrap_func

def func_needs_decorator():
    print("I want to be decorated!!")


func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)

decorated_func()





# +
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")


# -

func_needs_decorator()

# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()





@new_decorator
def func_needs_decorator():
    print("I want to be decorated")


func_needs_decorator()


