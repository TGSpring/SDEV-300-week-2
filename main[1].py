"""Tyler Spring
Lab 2
SDEV 300
"""

import datetime
import math
import random
import string
import sys

"""The menu that prompts the user to select an option"""
user = input(
    "Enter one of the options:\nPassword, \nCalculate and Format Perecentage, "
    "\nHow many days from today until "
    "\nJuly 4, 2025, \nUse the Law of Cosines to calculate the leg of a triangle, "
    "\nCalculate the volume of"
    " a Right Circular Cylinder, \nExit")


def uppercase():
    """
Function to create password of upper case letters. Uses sample.
    """
    string_upper = string.ascii_uppercase
    string_upper = random.sample(string_upper, wordlen)
    print("Your new password of upper case letters: ", string_upper)


def lowercase():
    """
Function to create password of lower case letters. Uses sample.
    :rtype: object
    """
    string_lower = string.ascii_lowercase
    string_lower = random.sample(string_lower, wordlen)
    print("Your new password of special lower case letters: ", string_lower)


def numbers():
    """
Function to create password of number. Uses sample.
    :rtype: object
    """
    number_pass = string.digits
    number_pass = random.sample(number_pass, wordlen)
    print("Your new password of special numbers: ", number_pass)


def special():
    """
Function to create password of special characters. Uses sample.
    :rtype: object
    """
    spec = string.punctuation
    spec = random.sample(spec, wordlen)
    print("Your new password of special characters: ", spec)


"""The main if body that asks the user the length of the password, to choose their type of password,
then calls the selected function to generate it."""
if user == "Password":
    wordlen = int(input("Enter the length of the password."))
    if wordlen == 0:
        wordlen = int(input("Invalid. ReEnter:"))
        case = input("Did you want uppercase, lowercase, numbers or special characters in it?")
        if case == "uppercase":
             uppercase()
        elif case == "lowercase":
             lowercase()
        elif case == "numbers":
             numbers()
        elif case == "special":
             special()
    else:
     case = input("Invalid. Please select either uppercase, "
                 "lowercase, numbers or special characters.")

def formatter():
    """
Function that formats input from user when the select
percentage and outputs it after validation
and calculation.
    :rtype: object
    """
    form = float(input("Enter your first number."))
    form_1 = float(input("Enter your second number."))
    if form_1 >= form:
        ans = form_1 / form
        print("Percentage and formatted number:  %.2f" % ans)
    elif form >= form_1:
        print("Incorrect input. ReEnter.")
        formatter()


"""Checks if user selected percentage from menu. Calls function"""
if user == "percentage":
    formatter()


def days():
    """
Calculates the amount of days from the current day of running to July 4th, 2025.
    :rtype: object
    """
    inDay = datetime.date.today()
    valDay = datetime.date(2025, 7, 4)
    diffDay = valDay - inDay
    print("The difference in the days from today to July 4th, 2025 are: ", diffDay.days)


"""Checks if user selected days from menu. 
Calls function"""
if user == "days":
    days()


def cosine():
    """
Function that asks user for measurements of a triangle in order to calculate the length of a leg.
    :rtype: object
    """
    leg_1 = float(input("Enter leg length."))
    if leg_1 <= 0:
        print("Invalid, reEnter:")
        leg_1 = float(input("Enter leg length."))
    leg_2 = float(input("Enter leg length."))
    if leg_2 <= 0:
        print("Invalid, reEnter:")
        leg_2 = float(input("Enter leg length."))
    side_1 = float(input("Enter a opposite side angle: "))
    if side_1 <= 0:
        print("Invalid, reEnter:")
        side_1 = float(input("Enter leg length."))
    side_1 = math.sqrt(leg_1 * leg_1 + leg_2 * leg_2 - 2 * leg_1 * leg_2 * math.cos(math.radians(side_1)))

    print("The length of the leg of the triangle is: %.2f" % side_1)


"""Checks if user selected cosine from menu. Calls function"""
if user == "cosine":
    cosine()


def right_c():
    """
Calculates the volume of a cylinder by asking the user for the radius and height.
    :rtype: object
    """
    rad = float(input("Enter the radius of the cylinder."))
    if rad <= 0:
        print("Invalid. ReEnter.")
        rad = float(input("Enter the radius of the cylinder."))
    hei = float(input("Enter the height of the cylinder."))
    if hei <= 0:
        print("Invalid. ReEnter.")
        hei = float(input("Enter the height of the cylinder."))
    vol = math.pi * rad * rad * hei
    print("Volume of the cylinder is:  %.2f" % vol)


"""Checks to see if the user selects exit, then exits the program."""
if user == "right":
    right_c()
if user == "exit":
    sys.exit()
