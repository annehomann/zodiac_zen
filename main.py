""" 
This is the docstring 
"""
from bs4 import BeautifulSoup
import requests
import os
import datetime
import emoji

datestamp = datetime.datetime.now()
print (datestamp.strftime('\n%A, %B %d, %Y \n%I:%M:%S %p\n'))

def menu():
    while True:
        print('Welcome to Zodiac Zen! Please select an option...')
        print('(1) What is my star sign?')
        print('(2) Receive my daily horoscope')
        print('(3) Exit')
        user_input = input('\n')

        if user_input == '1':
            astro()                       
        elif user_input == '2':
            readings()
        elif user_input == '3':
            print('Thank you for using Zodiac Zen! Goodbye \U0001F600')
            break
        else:
            print('Sorry, try again. Choose one from above')

def astro():
    day = int(input("What is your birth date: "))
    month = input("What is your birth month: ").strip()
    if month == 'december':
        astro_sign = 'sagittarius - the archer.\n' if (day < 22) else 'capricorn - the goat.\n'
    elif month == 'january':
        astro_sign = 'capricorn - the goat.\n' if (day < 20) else 'aquarius - the water bearer.\n'
    elif month == 'february':
        astro_sign = 'aquarius - the water bearer.\n' if (day < 19) else 'pisces - the fishes.\n'
    elif month == 'march':
        astro_sign = 'pisces - the fishes.\n' if (day < 21) else 'aries - the ram.\n'
    elif month == 'april':
        astro_sign = 'aries - the ram.\n' if (day < 20) else 'taurus - the bull.\n'
    elif month == 'may':
        astro_sign = 'taurus - the bull.\n' if (day < 21) else 'gemini - the twins.\n'
    elif month == 'june':
        astro_sign = 'gemini - the twins.\n' if (day < 21) else 'cancer - the crab.\n'
    elif month == 'july':
        astro_sign = 'cancer - the crab.\n' if (day < 23) else 'leo - the lion.\n'
    elif month == 'august':
        astro_sign = 'leo - the lion.\n' if (day < 23) else 'virgo - the virgin.\n'
    elif month == 'september':
        astro_sign = 'virgo - the virgin.\n' if (day < 23) else 'libra - the balance.\n'
    elif month == 'october':
        astro_sign = 'libra - the balance.\n' if (day < 23) else 'scorpio - the scorpian.\n'
    elif month == 'november':
        astro_sign = 'scorpio - the scorpian.\n' if (day < 22) else 'sagittarius - the archer.\n'
    print(f"\nYour Astrological sign is: {astro_sign.title()}")

def readings():
    url = 'http://annehomann.github.io/astro.html'
    r = requests.get(url)
    s = BeautifulSoup(r.content, 'html.parser')
    #find text, get only text, append to list
    horoscope = []
    for text in s.find_all("p"):
        b = text.get_text().strip()
        horoscope.append(b)

    user_sign = (input("Please enter your star sign: ")).strip()
    if user_sign == 'capricorn': 
        print('\n' + horoscope[0] + '\n')
        print('\nWould you like to save a copy of your horoscope?\nY/N?\n')
        answer = input()
        if answer == 'Y':
            with open ("capricorn" + '.txt', 'w') as file:
                file.write(horoscope[0])
        elif answer == 'N':
            exit
    elif user_sign == 'aquarius':
        print('\n' + '\t\t' + horoscope[1] + '\n')
        print('\nWould you like to save a copy of your horoscope?\nY/N?\n')
        answer = input()
        if answer == 'Y':
            with open ('aquarius' + '.txt', 'w') as file:
                file.write(horoscope[1])
        elif answer == 'N':
            exit            
    elif user_sign == 'pisces':
        print('\n' + '\t\t' + horoscope[2] + '\n')
        print('\nWould you like to save a copy of your horoscope?\nY/N?\n')
        answer = input()
        if answer == 'Y':
            with open ('pisces' + '.txt', 'w') as file:
                file.write(horoscope[2])
        elif answer == 'N':
            exit  
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
