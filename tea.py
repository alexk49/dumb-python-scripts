"""Implementation of tea mug:
var tea = new tea

if (tea.IsEmpty())
{
    tea.Refill();
}
else
{
    tea.Drink();
}
"""

print("Hello, have some tea!")
number_of_cups = int(input("How many cups of tea would you like? "))

class Tea:
    def __init__(self, state):
        """Create new tea object"""
        print("A new cup of tea has been made!")
        # state should be full, empty or neither
        self.state = state

    def IsEmpty(self):
        if tea.state == "empty":
            print("Oh no, you've run out of tea.")
            return True
        elif tea.state == "full":
            print("You've still got a full mug to go.")
        else:
            print("There's still a bit left")

    def Refill(self):
        print("Let me fill that up for you.")
        tea.state = "full"

    def Drink(self):
        print("Delicious tea!")
        tea.state = "empty"


tea = Tea("full")

for n in range(number_of_cups):
    if tea.IsEmpty():
        tea.Refill()
    else:
        tea.Drink()
