import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
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
    first_number = float(input("Podaj składnik 1: "))
    second_number = float(input("Podaj składnik 2: "))
    calc_info = {
    "1": f"Dodaję {first_number} i {second_number}",
    "2": f"Odejmuję {second_number} od {first_number}",
    "3": f"Mnożę {first_number} i {second_number}",
    "4": f"Dzielę {first_number} przez {second_number}"
    }
    logging.info(calc_info[f"{sign}"])
    calc_result = calc(sign, first_number, second_number)
    print(f"Wynik to: {calc_result}")