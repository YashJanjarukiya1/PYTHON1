#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yashp
#
# Created:     26-11-2022
# Copyright:   (c) yashp 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

first = input("enter the first number:")

operator = input("enter operator (+,-,*,/,%):")

second = input("entre the second number:")

first = int(first)

second = int(second)

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/":
    print(first / second)

elif operator == "%":
    print(first % second)

else:
    print("invalied operation")
