import math
from fractions import Fraction

def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y == 0:
        return "Błąd: Dzielenie przez zero!"
    else:
        return x / y

def potegowanie(x, y):
    return x ** y

def pierwiastkowanie(x):
    if x < 0:
        return "Błąd: Pierwiastkowanie liczby ujemnej!"
    else:
        return math.sqrt(x)

def logarytm(x, base=10):
    if x <= 0:
        return "Błąd: Logarytm z liczby niedodatniej!"
    else:
        return math.log(x, base)

def sinus(x):
    return math.sin(math.radians(x))

def cosinus(x):
    return math.cos(math.radians(x))

def tangens(x):
    return math.tan(math.radians(x))

def cotangens(x):
    if math.tan(math.radians(x)) == 0:
        return "Błąd: Cotangens niezdefiniowany!"
    else:
        return 1 / math.tan(math.radians(x))

def informacje():
    print("Informacje o Kalkulatorze Aurapi")
    print("===============================")
    print("Wersja: beta 0.1.0")
    print("Autor: Kropelek")
    print("Data Utworzenia: 2024-06-30")
    print("Opis: Aurapi to zaawansowany kalkulator obsługujący podstawowe i zaawansowane funkcje matematyczne.")

def menu():
    print("Aurapi - Zaawansowany Kalkulator")
    print("==============================")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Pierwiastkowanie")
    print("7. Logarytm")
    print("8. Sinus")
    print("9. Cosinus")
    print("10. Tangens")
    print("11. Cotangens")
    print("12. Informacje")
    print("0. Zakończ")

def get_fraction_input(prompt):
    while True:
        try:
            return Fraction(input(prompt))
        except ValueError:
            print("Nieprawidłowy format. Spróbuj ponownie.")

def main():
    while True:
        menu()
        wybor = input("Wybierz numer operacji (0-12): ")

        if wybor == '0':
            print("Koniec programu.")
            break
        elif wybor == '12':
            informacje()
            input("Naciśnij dowolny klawisz, aby kontynuować.")
            continue

        if wybor in {'1', '2', '3', '4', '5'}:
            liczba1 = get_fraction_input("Podaj pierwszą liczbę (ułamek w formacie a/b lub liczba całkowita): ")
            liczba2 = get_fraction_input("Podaj drugą liczbę (ułamek w formacie a/b lub liczba całkowita): ")

        if wybor == '1':
            wynik = dodawanie(liczba1, liczba2)
        elif wybor == '2':
            wynik = odejmowanie(liczba1, liczba2)
        elif wybor == '3':
            wynik = mnozenie(liczba1, liczba2)
        elif wybor == '4':
            wynik = dzielenie(liczba1, liczba2)
        elif wybor == '5':
            wynik = potegowanie(liczba1, liczba2)
        elif wybor == '6':
            liczba = get_fraction_input("Podaj liczbę do pierwiastkowania: ")
            wynik = pierwiastkowanie(float(liczba))
        elif wybor == '7':
            liczba = get_fraction_input("Podaj liczbę do logarytmowania: ")
            base = get_fraction_input("Podaj podstawę logarytmu (domyślnie 10): ") or 10
            wynik = logarytm(float(liczba), float(base))
        elif wybor == '8':
            liczba = float(input("Podaj kąt w stopniach do obliczenia sinusa: "))
            wynik = sinus(liczba)
        elif wybor == '9':
            liczba = float(input("Podaj kąt w stopniach do obliczenia cosinusa: "))
            wynik = cosinus(liczba)
        elif wybor == '10':
            liczba = float(input("Podaj kąt w stopniach do obliczenia tangensa: "))
            wynik = tangens(liczba)
        elif wybor == '11':
            liczba = float(input("Podaj kąt w stopniach do obliczenia cotangensa: "))
            wynik = cotangens(liczba)
        else:
            wynik = "Nieprawidłowy wybór operacji."

        print(f"Wynik: {wynik}")
        input("Naciśnij dowolny klawisz, aby kontynuować.")
        print("\n")

if __name__ == "__main__":
    main()
