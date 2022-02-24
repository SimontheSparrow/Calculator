
import logging
import numbers
import sys
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Choose and check operation
try:
    operation = int(input(
        " Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

except:
    print("Niepoprawny format")
    sys.exit(1)


# Choose and check numbers
if operation == 2 or operation == 4:
    try:
        first_num = float(input("Pierwsza liczba: "))
        second_num = float(input("Druga liczba: "))
    except:
        print("Niepoprawny format")
        sys.exit(1)

elif operation == 1 or operation == 3:
    try:
        numbs_list = [float(numbs_list)
                      for numbs_list in input("Wprowadź wartości: ").split()]
    except:
        print("Niepoprawny format")
        sys.exit(1)


# Define calculating functions

def calclulate_two_or_four(operation, first_num, second_num):
    if operation == 2:
        logging.info(f"Odejmuję {first_num} i {second_num}")
        print(f"Wynik to {round(first_num - second_num, 2)}")

    elif operation == 4:
        logging.info(f"Dzielę {first_num} i {second_num}")
        print(f"Wynik to {round(first_num / second_num, 2)}")


def calclulate_one_or_three(operation, numbs_list):    
    if operation == 1:
        result = 0
        for number in numbs_list:
            result += number
        print("Dodaję", end=' ')
        for number in numbs_list:
            print(number, end=' ')
        print(f"\nWynik to {result}")

    elif operation == 3:
        result = 1
        for number in numbs_list:
            result *= number
        print("Mnożę", end=' ')
        for number in numbs_list:
            print(number, end=' ')
        print(f"\nWynik to {result}")


# Calculate
if operation == 2 or operation == 4:
    calclulate_two_or_four(operation, first_num, second_num)

elif operation == 1 or operation == 3:
    calclulate_one_or_three(operation, numbs_list)

