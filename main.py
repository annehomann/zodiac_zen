#!/usr/bin/python3
"""
Program: Zodiac Zen
Author: Anne Homann
Contact: css011906@coderacademy.edu.au
Date: 2019/06/29
Licence: GPLv3
Version: 0.1
"""
import datetime
import argparse
import requests
from bs4 import BeautifulSoup
from colorama import Back, Style

# Shows current day and time to user
DATESTAMP = datetime.datetime.now()
print(DATESTAMP.strftime('\n\t%A, %B %d, %Y'))

def greeting():
    """ A personaized greeting for the user """
    first = input("\n\tWelcome! What is your first name? ")
    last = input("\tAnd your last name? ")
    print(Back.BLUE)
    print(f"\n\tHello {first} {last}! \U0001F607")

def menu():
    """ Main user menu for the program """
    while True:
        print(Back.BLUE)
        print('\n\t\U0001F525 WELCOME TO ZODIAC ZEN!')
        print('\n\tPRESS EITHER 1, 2 OR 3 TO MAKE YOUR SELECTION')
        print(Style.RESET_ALL)
        print('\n\t(1) What is my star sign?')
        print('\t(2) Receive my daily horoscope')
        print('\t(3) Exit')
        user_input = input('\n\t')

        # Option 1 calls the astro function
        if user_input == '1':
            astro()
        # Option 2 calls the get_sign function and stores the user's input into the sign variable
        # Then the get_readings function is called with signs as an argument
        elif user_input == '2':
            sign = get_sign()
            get_readings(sign)
        # Option 3 is Exit
        elif user_input == '3':
            print('\n\tThank you for using Zodiac Zen! Goodbye \U0001F44B\n')
            break
        else:
            print('\n\tSorry, try again. Choose one from above')

def astro():
    """ Gets the user's birth date and month and outputs
        their astrological star sign """
    # Error handling for invalid input
    while True:
        try:
            day = int(input("\n\tWhat day of the month were you born? (numbers only): "))
            if day < 1 or day > 31:
                raise ValueError
            break
        except ValueError:
            print("\tInvalid birth date! It must be in the range of 1-31.")
    while True:
        try:
            month = str(input("\n\tWhat month were you born?: ")).strip().lower()
            if month not in ('january', 'february', 'march', 'april', 'may', 'june',
            'july', 'august', 'september', 'october', 'november', 'december'):
                raise TypeError
            break
        except TypeError:
            print("\tInvalid birth month! Please try again.")
    # Start of conditional statement for star signs
    if month == 'december':
        astro_sign = '\U00002650 sagittarius\n' if (day < 22) else '\U00002651 capricorn\n'
    elif month == 'january':
        astro_sign = '\U00002651 capricorn\n' if (day < 20) else '\U00002652 aquarius\n'
    elif month == 'february':
        astro_sign = '\U00002652 aquarius\n' if (day < 19) else '\U00002653 pisces\n'
    elif month == 'march':
        astro_sign = '\U00002653 pisces\n' if (day < 21) else '\U00002648 aries\n'
    elif month == 'april':
        astro_sign = '\U00002648 aries\n' if (day < 20) else '\U00002649 taurus\n'
    elif month == 'may':
        astro_sign = '\U00002649 taurus\n' if (day < 21) else '\U0000264A gemini\n'
    elif month == 'june':
        astro_sign = '\U0000264A gemini\n' if (day < 21) else '\U0000264B cancer\n'
    elif month == 'july':
        astro_sign = '\U0000264B cancer\n' if (day < 23) else '\U0000264C leo\n'
    elif month == 'august':
        astro_sign = '\U0000264C leo\n' if (day < 23) else '\U0000264D virgo\n'
    elif month == 'september':
        astro_sign = '\U0000264D virgo\n' if (day < 23) else '\U0000264E libra\n'
    elif month == 'october':
        astro_sign = '\U0000264E libra\n' if (day < 23) else '\U0000264F scorpio\n'
    elif month == 'november':
        astro_sign = '\U0000264F scorpio\n' if (day < 22) else '\U00002650 sagittarius\n'
    print(Back.RED)
    print(f'\n\tYour Astrological sign is: {astro_sign.title()}')
    print(Style.RESET_ALL)

DATE_READING = datetime.datetime.now()
# Global variable to store daily horoscope readings
HOROSCOPE = []
def web_scrape():
    """ Scrapes HTML and adds each paragraph
    to an index in a list"""
    url = 'http://annehomann.github.io/astro.html'
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    #find text, get only text, append to list
    for text in soup.find_all("p"):
        block = text.get_text().strip()
        HOROSCOPE.append(block)

def get_sign():
    """ Ask the user for their star sign """
    # Error handling for invalid input
    while True:
        try:
            user_sign = (input("\n\tPlease enter your star sign: ")).strip().lower()
            web_scrape()
            if user_sign not in ('capricorn', 'aquarius', 'pisces', 'aries', 'taurus',
            'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius'):
                raise TypeError
            return user_sign
        except TypeError:
            print("\tInvalid star sign! Please try again.")

def get_readings(sign):
    """ Takes the user's input and retrieves the
    correct hororscope then asks them to save to file"""
    print('\t' + sign.upper())
    # Start of conditional statement for horoscope readings
    if sign == "capricorn":
        print('\n' + '\t\t' + HOROSCOPE[0] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('capricorn_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[0])
    elif sign == "aquarius":
        print('\n' + '\t\t' + HOROSCOPE[1] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('aquarius_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[1])
    elif sign == "pisces":
        print('\n' + '\t\t' + HOROSCOPE[2] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('pisces_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[2])
    elif sign == "aries":
        print('\n' + '\t\t' + HOROSCOPE[3] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('aries_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[3])
    elif sign == "taurus":
        print('\n' + '\t\t' + HOROSCOPE[4] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('taurus_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[4])
    elif sign == "gemini":
        print('\n' + '\t\t' + HOROSCOPE[5] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('gemini_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[5])
    elif sign == "cancer":
        print('\n' + '\t\t' + HOROSCOPE[6] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('cancer_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[6])
    elif sign == "leo":
        print('\n' + '\t\t' + HOROSCOPE[7] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('leo_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[7])
    elif sign == "virgo":
        print('\n' + '\t\t' + HOROSCOPE[8] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('virgo_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[8])
    elif sign == "libra":
        print('\n' + '\t\t' + HOROSCOPE[9] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('libra_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[9])
    elif sign == "scorpio":
        print('\n' + '\t\t' + HOROSCOPE[10] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('scorpio_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[10])
    elif sign == "sagittarius":
        print('\n' + '\t\t' + HOROSCOPE[11] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('sagittarius_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(HOROSCOPE[11])

# Argparse
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-r', '--reading', help='Daily Horoscope Reading')
    MYARGS = PARSER.parse_args()

    SIGN = MYARGS.reading

    if MYARGS.reading == None:
        greeting()
        menu()
    else:
        web_scrape()
        get_readings(SIGN)
