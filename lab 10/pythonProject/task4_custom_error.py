class LowPriceError(Exception):
    pass

try:
    price = int(input("Тауар бағасын енгізіңіз: "))

    if price < 1000:
        raise LowPriceError("Баға өте төмен! Дүкенде мұндай арзан тауар болмайды.")

    print("Баға қабылданды.")

except LowPriceError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Баға сан болуы керек!")