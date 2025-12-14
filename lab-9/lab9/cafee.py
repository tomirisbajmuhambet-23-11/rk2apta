class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = float(price)

    def __str__(self):
        return f"{self.name} - {self.price:.2f}₸"

class Customer:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Order:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.items = []
    def add_item(self, menu_item: MenuItem, quantity: int = 1):
        for _ in range(quantity):
            self.items.append(menu_item)
    def total(self) -> float:
        return sum(item.price for item in self.items)

    def receipt(self) -> str:
        lines = []
        lines.append(f"Түбіртек — Клиент: {self.customer.name}")
        if not self.items:
            lines.append("Тапсырыс бос.")
            return "\n".join(lines)
        summary = {}
        for it in self.items:
            summary.setdefault(it.name, {"price": it.price, "qty": 0})
            summary[it.name]["qty"] += 1
        lines.append("-" * 30)
        for name, info in summary.items():
            lines.append(f"{name} x{info['qty']} — {info['price']:.2f}₸ each")
        lines.append("-" * 30)
        lines.append(f"Жалпы: {self.total():.2f}₸")
        return "\n".join(lines)

class Cafe:
    def __init__(self, name: str):
        self.name = name
        self.menu = []
        self.orders = []

    def add_menu_item(self, item: MenuItem):
        self.menu.append(item)
    def show_menu(self):
        print(f"\n{self.name} мәзірі:")
        for idx, item in enumerate(self.menu, start=1):
            print(f"{idx}. {item}")
    def create_order(self, customer_name: str, selections: list):
        customer = Customer(customer_name)
        order = Order(customer)
        for idx, qty in selections:
            if 1 <= idx <= len(self.menu):
                order.add_item(self.menu[idx - 1], quantity=qty)
            else:
                print(f"Ескерту: мәзірде {idx} нөмірі жоқ — өткізіп жіберілді.")
        self.orders.append(order)
        return order

    def show_orders(self):
        print(f"\n{self.name} тапсырыстары (жалпы {len(self.orders)}):")
        for i, ord in enumerate(self.orders, start=1):
            print(f"\nТапсырыс #{i}")
            print(ord.receipt())

def parse_selection_input(s: str):
    s = s.strip()
    if not s:
        return []
    parts = [p.strip() for p in s.split(",")]
    out = []
    for p in parts:
        if "x" in p:
            try:
                idx_str, qty_str = p.split("x")
                idx = int(idx_str)
                qty = int(qty_str)
            except ValueError:
                print(f"Қате формат: '{p}', өткізіліп жатыр.")
                continue
        else:
            try:
                idx = int(p)
                qty = 1
            except ValueError:
                print(f"Қате формат: '{p}', өткізіліп жатыр.")
                continue
        out.append((idx, qty))
    return out
def main():
    cafe = Cafe("Асыл Дәм Кафе")
    cafe.add_menu_item(MenuItem("Эспрессо", 600))
    cafe.add_menu_item(MenuItem("Капучино", 900))
    cafe.add_menu_item(MenuItem("Латте", 1000))
    cafe.add_menu_item(MenuItem("Чай", 400))
    cafe.add_menu_item(MenuItem("Сэндвич", 1200))
    cafe.add_menu_item(MenuItem("Торттың бір бөлігі", 800))

    print(f"Қош келдіңіз — {cafe.name}!\n")
    cafe.show_menu()
    customer_name = input("\nКлиенттің аты: ").strip()
    sel = input("Таңдауларды нөмір арқылы енгізіңіз (мысалы: 1,2x2,5): ").strip()
    selections = parse_selection_input(sel)

    order = cafe.create_order(customer_name, selections)
    print("\nТапсырыс қабылданды. Түбіртек:\n")
    print(order.receipt())
if __name__ == "__main__":
    main()