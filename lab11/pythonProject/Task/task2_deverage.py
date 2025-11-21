class Beverage:
    def describe(self):
        print("This is a beverage.")

class Tea(Beverage):
    def describe(self):
        print("Tea: warm and refreshing.")

b = Beverage()
t = Tea()

b.describe()
t.describe()