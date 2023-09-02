class ClassWithProperties:
    def __init__(self):
        self.someAttribute = "some initial value"

    @property
    def someAttribute(self):  # This is a getter method
        return self._someAttribute

    @someAttribute.setter
    def someAttribute(self, value):  # this is a setter method
        self._someAttribute = value

    @someAttribute.deleter
    def someAttribute(self):  # This is the deleter method
        del self._someAttribute


obj = ClassWithProperties()
print(obj.someAttribute)
obj.someAttribute = "changed value"
print(obj.someAttribute)  # Prints 'changed value'
del obj.someAttribute  # Deletes the attribute
