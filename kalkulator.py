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
        exit(1)
    return result


if __name__ == "__main__":
    sign = int(sys.argv[1])
    first_number = float(sys.argv[2])
    second_number = float(sys.argv[3])
calc_result = calc(sign, first_number, second_number)
print(calc_result)

