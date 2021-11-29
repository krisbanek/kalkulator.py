import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def calc(sign, first_number, second_number):
    if sign == 1:
        logging.info(f"Dodaję {first_number} i {second_number}.")
    elif sign == 2:
        logging.info(F"Odejmuję {second_number} od {first_number}.")      
    elif sign == 3:
        logging.info(f"Mnożę {first_number} i {second_number}.")    
    elif sign == 4:
        logging.info(f"Dzielę {first_number} przez {second_number}.")    
    else:
        logging.info("Wybrałeś złą liczbę opisującą działanie. \n Uruchom skrypt ponownie używając liczb z zakresu 1 - 4.")
        exit(1)
    result = calc_dict[f"{sign}"]
    return result

if __name__ == "__main__":
    sign = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    first_number = float(input("Podaj składnik 1: "))
    second_number = float(input("Podaj składnik 2: "))

calc_dict = {
    "1": f"{first_number + second_number}",
    "2": f"{first_number - second_number}",
    "3": f"{first_number * second_number}",
    "4": f"{first_number / second_number}"
}
calc_result = calc(sign, first_number, second_number)
print(f"Wynik to: {calc_result}")

