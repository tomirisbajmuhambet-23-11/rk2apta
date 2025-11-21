class Dish:
    def __init__(self, name, price):   # ДҰРЫС
        self.name = name
        self.price = price

    def info(self):
        print(f"Dish: {self.name}, Price: {self.price}₸")


class MainDish(Dish):
    def __init__(self, name, price, calories):   # ДҰРЫС
        super().__init__(name, price)
        self.calories = calories

    def info(self):
        print(f"Dish: {self.name}, Price: {self.price}₸, Calories: {self.calories} kcal")


food = MainDish("Beshbarmak", 2500, 850)
food.info()
