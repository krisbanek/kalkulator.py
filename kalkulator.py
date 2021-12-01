import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def add(first_number, second_number):
    logging.info(f"Dodaję: {first_number} i {second_number}")
    return first_number + second_number

def subtract(first_number, second_number):
    logging.info(f"Odejmuję: {second_number} od {first_number}")
    return first_number - second_number

def multiply(first_number, second_number):
    logging.info(f"Mnożę: {first_number} i {second_number}")
    return first_number * second_number

def divide(first_number, second_number):
    logging.info(f"Dzielę: {first_number} przez {second_number}")
    return first_number / second_number

calc_dict = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide
    }

def calc(sign, first_number, second_number):
    method = calc_dict[f"{sign}"]
    return method(first_number, second_number)

if __name__ == "__main__":
    sign = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    if sign >= 1 and sign <=4:
        pass
    else:
        logging.info("Nie wybrałeś liczby z zakresu 1 - 4. Podaj poprawną liczbę odpowiadającą działaniu: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie.")
        exit(1)
    first_number = float(input("Podaj składnik 1: "))
    second_number = float(input("Podaj składnik 2: "))
    calc_result = calc(sign, first_number, second_number)
    print(f"Wynik to: {calc_result}")