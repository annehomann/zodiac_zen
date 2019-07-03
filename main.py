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
print(DATESTAMP.strftime('\n%A, %B %d, %Y'))

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

        if user_input == '1':
            astro()
        elif user_input == '2':
            readings()
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
def readings():
    """ Scrapes HTML and adds each paragraph
    to an index in a list"""
    url = 'http://annehomann.github.io/astro.html'
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    #find text, get only text, append to list
    horoscope = []
    for text in soup.find_all("p"):
        block = text.get_text().strip()
        horoscope.append(block)
    
    # Error handling for invalid inout
    while True:
        try:
            user_sign = (input("\n\tPlease enter your star sign: ")).strip().lower()
            if user_sign not in ('capricorn', 'aquarius', 'pisces', 'aries', 'taurus',
            'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius'):
                raise TypeError
            break
        except TypeError:
            print("\tInvalid star sign! Please try again.")
    # Start of conditional statement for horoscope readings
    if user_sign == 'capricorn':
        print('\n' + horoscope[0] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open("capricorn_" + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[0])
    elif user_sign == 'aquarius':
        print('\n' + '\t\t' + horoscope[1] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('aquarius_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[1])
    elif user_sign == 'pisces':
        print('\n' + '\t\t' + horoscope[2] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('pisces_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[2])
    elif user_sign == 'aries':
        print('\n' + '\t\t' + horoscope[3] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('aries_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[3])
    elif user_sign == 'taurus':
        print('\n' + '\t\t' + horoscope[4] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('taurus_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[4])
    elif user_sign == 'gemini':
        print('\n' + '\t\t' + horoscope[5] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('gemini_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[5])
    elif user_sign == 'cancer':
        print('\n' + '\t\t' + horoscope[6] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('cancer_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[6])
    elif user_sign == 'leo':
        print('\n' + '\t\t' + horoscope[7] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('leo_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[7])
    elif user_sign == 'virgo':
        print('\n' + '\t\t' + horoscope[8] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('virgo_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[8])
    elif user_sign == 'libra':
        print('\n' + '\t\t' + horoscope[9] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('libra_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[9])
    elif user_sign == 'scorpio':
        print('\n' + '\t\t' + horoscope[10] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('scorpio_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[10])
    elif user_sign == 'saggitarius':
        print('\n' + '\t\t' + horoscope[11] + '\n')
        print('\n\tWould you like to save a copy of your horoscope?\n\tY/N?\n')
        answer = input('\t').upper()
        if answer == 'Y':
            with open('saggitarius_' + DATE_READING.strftime('%B %d, %Y') + '.txt', 'w') as file:
                file.write(horoscope[11])

menu()

PARSER = argparse.ArgumentParser()
PARSER.add_argument('-e', '--element', help='Find out element by entering star sign', required=True)
ARGS = PARSER.parse_args()

if __name__ == "__main__":
    if ARGS.element == 'capricorn':
        print("Earth Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'virgo':
        print("Earth Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'taurus':
        print("Earth Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'aquarius':
        print("Air Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'gemini':
        print("Air Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'libra':
        print("Air Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'aries':
        print("Fire Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'leo':
        print("Fire Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'sagittarius':
        print("Fire Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'pisces':
        print("Water Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'cancer':
        print("Water Element: {}".format(ARGS.element).title())
    elif ARGS.element == 'scorpio':
        print("Water Element: {}".format(ARGS.element).title())
