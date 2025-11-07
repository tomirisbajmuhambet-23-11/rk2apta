with open("products.txt", "r", encoding="utf-8") as file:
    prices = []
    for line in file:
        product, price = line.strip().split(", ")
        prices.append(int(price))
        print(f"Тауар: {product} — Бағасы: {price} теңге")

    print("\nДүкендегі орташа баға:", sum(prices) / len(prices), "теңге")