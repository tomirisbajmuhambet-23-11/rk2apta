class Chef:
    def role(self):
        print("Cooking delicious meals.")

class Manager:
    def role(self):
        print("Managing restaurant operations.")

class HeadChef(Chef, Manager):
    def role(self):
        super().role()
        print("Also supervising all staff.")

h = HeadChef()
h.role()