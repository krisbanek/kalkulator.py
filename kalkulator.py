import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calc(sign, first_number, second_number):
    if sign == 1:
        logging.info(("Dodaję %s i %s.") %(first_number, second_number))
        result = first_number + second_number
    elif sign == 2:
        logging.info(("Odejmuję %s od %s.") %(second_number, first_number))
        result = first_number - second_number
    elif sign == 3:
        logging.info(("Mnożę %s i %s.") %(first_number, second_number))
        result = first_number * second_number
    elif sign == 4:
        logging.info(("Dzielę %s przez %s.") %(first_number, second_number))
        result = first_number / second_number
    else:
        logging.info("Wybrałeś złą liczbę opisującą działanie. \n Uruchom skrypt ponownie używając liczb z zakresu 1 - 4.")
        exit(1)
    return result

if __name__ == "__main__":
    sign = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    first_number = float(input("Podaj składnik 1: "))
    second_number = float(input("Podaj składnik 2: "))
calc_result = calc(sign, first_number, second_number)
print(f"Wynik to: {calc_result}")

