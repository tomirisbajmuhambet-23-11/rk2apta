try:
    with open("products.txt", "r", encoding="utf-8") as file:
        data = file.readlines()

except FileNotFoundError:
    print("Қате: products.txt файлы табылмады!")

else:
    print("Файл сәтті оқылды:")
    for line in data:
        print(line.strip())

finally:
    print(" Бағдарлама орындалды.")