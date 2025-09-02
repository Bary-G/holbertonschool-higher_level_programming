#!/usr/bin/python3
number1 = 0
number2 = -1
while number1 < 99 :
    number2 = number2 + 1
    if number2 == 10 and number1 != 10 :
        number2 = number2 - 10
        number1 = number1 + 1
    print("{}{}".format(number1, number2), end="")
