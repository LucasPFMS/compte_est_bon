# This is a sample Python script.
import random


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def draw(numbers):
    choice: list = []
    n = 0
    while n < len(numbers):
        choice.append(random.choice(numbers))
        n += 1
    return choice
    # Use a breakpoint in the code line below to debug your script.
    #  Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    all_numbers: list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 50, 75, 100]


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
