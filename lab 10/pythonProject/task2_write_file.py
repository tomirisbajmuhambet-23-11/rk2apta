product = input("Тауар атауын енгізіңіз: ")
price = input("Бағасын енгізіңіз: ")

with open("products.txt", "a", encoding="utf-8") as file:
    file.write(f"\n{product}, {price}")

print("Жаңа тауар сәтті қосылды!")