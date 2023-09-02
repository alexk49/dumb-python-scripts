import wizcoin


class WizardCustomerWithInheritance(wizcoin.WizCoin):
    """Don't do this. There is no relationship between the two classes so inheritance creates some awkward code.
    The names wizard.value() and wizard.weightIngrams() method names are misleading as it seems to be the wizard's weight and value rather than the value and weight of the coins.
    """

    def __init__(self, name):
        self.name = name
        super().__init__(0, 0, 0)


class WizardCustomer:
    """With composition, the WizCoin object is used as an attribute instead of as an inherited class"""

    """This leads to more maintable code, and clearer code. See the second print out example which is much more precisely worded."""

    def __init__(self, name):
        self.name = name
        self.purse = wizcoin.WizCoin(0, 0, 0)


wizard = WizardCustomerWithInheritance("Alice")
print(f"{wizard.name} has {wizard.value()} knuts worth of money.")
print(f"{wizard.name}'s coins weigh {wizard.weightInGrams()} grams.")


wizard = WizardCustomer("Alice")
print(f"{wizard.name} has {wizard.purse.value()} knuts worth of money")
print(f"{wizard.name}'s coins weigh {wizard.purse.weightInGrams()} grams.")
