class Person:
    # runs on creation
    # includes standard data types for person class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # NOTE: you always have to pass self to class methods
    def say_hello(self):
        print("Hello, my name is: ", self.name)


    def say_age(self):
        print(f"Hello my name is {self.name}, and I am {self.age} years old.") 

# assign new class object
person = Person("Alex", 859)

person.say_hello()

person.say_age()
