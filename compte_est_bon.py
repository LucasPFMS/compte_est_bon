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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    all_numbers: list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100]
    m = 0
    my_numbers: list = []
    print("voici tes nombres: ")
    while m < 6:
        random_number = random.choice(all_numbers)
        draw(my_numbers, random_number)
        del_number(all_numbers, random_number)
        print(my_numbers[m])
        m += 1
    final = final_number()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
