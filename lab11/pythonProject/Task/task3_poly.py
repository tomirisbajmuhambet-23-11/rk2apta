class MenuItem:
    def get_price(self):
        pass

class Soup(MenuItem):
    def get_price(self):
        return 1200

class Dessert(MenuItem):
    def get_price(self):
        return 1500


items = [Soup(), Dessert()]

for item in items:
    print("Price:", item.get_price(), "T")