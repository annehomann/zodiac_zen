"""
This is the docstring
"""
import datetime
import requests
#import argparse
from bs4 import BeautifulSoup
from colorama import Back, Style

DATESTAMP = datetime.datetime.now()
print(DATESTAMP.strftime('\n%A, %B %d, %Y \n'))

def menu():
    """ FUNCTION DOCSTRING """
    while True:
        print(Back.BLUE)
        print('\n\t\U0001F525 Welcome to Zodiac Zen! Please select an option...')
        print(Style.RESET_ALL)
        print('\n(1) What is my star sign?')
        print('(2) Receive my daily horoscope')
        print('(3) Exit')
        user_input = input('\n')

        if user_input == '1':
            astro()
        elif user_input == '2':
            readings()
        elif user_input == '3':
            print('Thank you for using Zodiac Zen! Goodbye \U0001F44B')
            break
        else:
            print('Sorry, try again. Choose one from above')

def astro():
    """ FUNCTION DOCSTRING """
    while True:
        try:
            day = int(input("What is your birth date: "))
            if day < 1 or day > 31:
                raise ValueError
            break
        except ValueError:
            print("Invalid birth date! It must be in the range of 1-31.")
    month = input("What is your birth month: ").strip().lower()
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

def readings():
    """ FUNCTION DOCSTRING """
    url = 'http://annehomann.github.io/astro.html'
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    #find text, get only text, append to list
    horoscope = []
    for text in soup.find_all("p"):
        block = text.get_text().strip()
        horoscope.append(block)

    user_sign = (input("Please enter your star sign: ")).strip().lower()
    if user_sign == 'capricorn':
        print('\n' + horoscope[0] + '\n')
        print('\nWould you like to save a copy of your horoscope?\nY/N?\n')
        answer = input()
        if answer == 'Y':
            with open("capricorn" + '.txt', 'w') as file:
                file.write(horoscope[0])
        else: exit
    elif user_sign == 'aquarius':
        print('\n' + '\t\t' + horoscope[1] + '\n')
        print('\nWould you like to save a copy of your horoscope?\nY/N?\n')
        answer = input()
        if answer == 'Y':
            with open('aquarius' + '.txt', 'w') as file:
                file.write(horoscope[1])
        else: exit
    elif user_sign == 'pisces':
        print('\n' + '\t\t' + horoscope[2] + '\n')
        print('\nWould you like to save a copy of your horoscope?\nY/N?\n')
        answer = input()
        if answer == 'Y':
            with open('pisces' + '.txt', 'w') as file:
                file.write(horoscope[2])
        else: exit
    elif user_sign == 'aries':
        print('\n' + '\t\t' + horoscope[3] + '\n')
    elif user_sign == 'taurus':
        print('\n' + '\t\t' + horoscope[4] + '\n')
    elif user_sign == 'gemini':
        print('\n' + '\t\t' + horoscope[5] + '\n')
    elif user_sign == 'cancer':
        print('\n' + '\t\t' + horoscope[6] + '\n')
    elif user_sign == 'leo':
        print('\n' + '\t\t' + horoscope[7] + '\n')
    elif user_sign == 'virgo':
        print('\n' + '\t\t' + horoscope[8] + '\n')
    elif user_sign == 'libra':
        print('\n' + '\t\t' + horoscope[9] + '\n')
    elif user_sign == 'scorpio':
        print('\n' + '\t\t' + horoscope[10] + '\n')
    elif user_sign == 'saggitarius':
        print('\n' + '\t\t' + horoscope[11] + '\n')
menu()
