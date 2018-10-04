__author__ = 'Герасимов Никита Алексеевич'

import math


# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
def MaxDigit(number):
    if not number.isdigit():
        exit()
    digits = [int(digit) for digit in str(number)]
    maxDigit = max(digits)
    return maxDigit


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
def SwapNumbers(a, b):
    if not a.isdigit() or not b.isdigit():
        exit()
    return b, a


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
def SolveEquation(a, b, c):
    if not a.isdigit() or not b.isdigit() or not c.isdigit():
        exit()
    a = int(a)
    b = int(b)
    c = int(c)
    d = 0
    try:
        d = math.sqrt((b * b) - (4 * a * c))
    except Exception as ex:
        print(ex)
        exit()
    x_1 = (d - b) / (2 * a)
    x_2 = (d + b) / (2 * a)
    return x_1, x_2


if __name__ == "__main__":
    # Работоспособность первой задачи
    userNumber = input("Input your number: ")
    print('Your number: {0}\n'
          'Max digit: {1}'.format(userNumber, MaxDigit(userNumber)))

    # Работоспособность второй задачи
    a = input("Input 1st number: ")
    b = input("Input 2nd number: ")
    x, y = SwapNumbers(a, b)
    print("Your numbers after swap = {0} and {1}".format(x, y))

    # Работоспособность третьей задачи
    a = input("Input a: ")
    b = input("Input b: ")
    c = input("Input c: ")
    x_1, x_2 = SolveEquation(a,b,c)
    print("Result: {0} and {1}".format(x_1, x_2))