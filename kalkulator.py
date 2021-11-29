import sys
import logging
logging.basicConfig(level=logging.DEBUG)
def calc(sign, first_number, second_number):
    if sign == 1:
        logging.info("Dodaję ")
        result = first_number + second_number
    elif sign == 2:
        logging.info("Odejmuję")
        result = first_number - second_number
    elif sign == 3:
        logging.info("Mnożę")
        result = first_number * second_number
    elif sign == 4:
        logging.info("Dzielę")
        result = first_number / second_number
    else:
        exit(1)
    return result


if __name__ == "__main__":
    sign = int(sys.argv[1])
    first_number = sys.argv[2]
    second_number = sys.argv[3]
calc_result = calc(sign, first_number, second_number)
print(calc_result)

