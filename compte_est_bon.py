# This is a sample Python script.
import random
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def draw(choice, number):
    choice.append(number)
    return choice
    # Use a breakpoint in the code line below to debug your script.
    #  Press Ctrl+F8 to toggle the breakpoint.


def del_number(numbers, number):
    numbers.remove(number)
    return numbers


def final_number():
    number = random.randint(101, 999)
    return number


def calculate(number_1, number_2, ope):
    if ope == "+":
        return number_1 + number_2
    elif ope == "-":
        return number_1 - number_2
    elif ope == "*":
        return number_1 * number_2
    elif ope == "/":
        return number_1 / number_2


def add_number(numbers, number):
    numbers.append(number)
    return numbers


def is_ending(the_end):
    end_game = input("Veux-tu t'arrêter ? o/n")
    if end_game == "o":
        return True
    else:
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    all_numbers: list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100]
    m = 0
    my_numbers: list = []
    print("Voici tes nombres: ")
    while m < 6:
        random_number = random.choice(all_numbers)
        draw(my_numbers, random_number)
        del_number(all_numbers, random_number)
        print(my_numbers[m])
        m += 1
    final = final_number()
    print("Tu dois arriver à : ", final)
    new_number = 0
    stop_game = False
    while new_number != final and len(my_numbers) != 1 and stop_game is False:
        first_number = int(input("Veuillez entrer un premier nombre parmis les tiens: "))
        del_number(my_numbers, first_number)
        my_operator = input("Choisis un oppérateur entre +,-,*,/")
        second_number = int(input("Veuillez entrer un second nombre parmis les tiens: "))
        del_number(my_numbers, second_number)
        new_number = calculate(first_number, second_number, my_operator)
        add_number(my_numbers, new_number)
        print("=", new_number)
        stop_game = is_ending(stop_game)
    if new_number == final:
        print("Le compte est bon !")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
