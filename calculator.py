import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(message)s')

try:
    operation = int(input(
        " Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

except:
    print("Niepoprawny format")
    sys.exit(1)


def calculate(operation):
    match operation:
        case 1:
            try:
                numbs_list = [float(numbs_list)
                              for numbs_list in input("Wprowadź wartości: ").split()]
            except:
                logging.info("Niepoprawny format")
                sys.exit(1)

            result = 0
            for number in numbs_list:
                result += number
            print("Dodaję", end=' ')
            for number in numbs_list:
                print(number, end=' ')
            logging.info(f"\nWynik to {result}")

        case 2:
            try:
                first_num = float(input("Pierwsza liczba: "))
                second_num = float(input("Druga liczba: "))
            except:
                logging.info("Niepoprawny format")
                sys.exit(1)

            logging.info(f"Odejmuję {first_num} i {second_num}")
            logging.info(f"Wynik to {round(first_num - second_num, 2)}")

        case 3:
            try:
                numbs_list = [float(numbs_list)
                              for numbs_list in input("Wprowadź wartości: ").split()]
            except:
                logging.info("Niepoprawny format")
                sys.exit(1)

            result = 1
            for number in numbs_list:
                result *= number
            print("Mnożę", end=' ')
            for number in numbs_list:
                print(number, end=' ')
            logging.info(f"\nWynik to {result}")

        case 4:
            try:
                first_num = float(input("Pierwsza liczba: "))
                second_num = float(input("Druga liczba: "))
            except:
                print("Niepoprawny format")
                sys.exit(1)

            logging.info(f"Dzielę {first_num} i {second_num}")
            logging.info(f"Wynik to {round(first_num / second_num, 2)}")


calculate(operation)
