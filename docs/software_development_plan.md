# Software Development Plan - Zodiac Zen



[Github](https://github.com/annehomann/zodiac_zen)

### <u>Statement of Purpose and Scope</u>

Zodiac Zen is a CLI that allows a user to find out their astrological sign, receive their daily horoscope reading and are given the option to download their daily reading to keep on file. This first option is available if the user does not know their star sign or would like to read the horoscope of a friend and/or family member. This is done by the user being asked to input their information, date of birth and month, to receive the correct star sign in return. The next option is if they would like to read their daily horoscope. This information is scraped from an astrology webpage using the python package BeautifulSoup4. The user will also be given the option to save the daily horoscope to a text file with a datestamp attached to the filename for easy reference.

There are countless astrological websites online that offer different horoscope readings for all signs and it is easy to get stuck in a rabbit hole of reading one after the other, which then becomes a big time waster. This program eliminates this and allows a more productive way of offering the user the information they seek on a daily basis, straight from their desktop in a speedy way. They can also store each horoscope reading into a folder for their own personal collection. 

The target audience for Zodiac Zen are astrology fans who like to frequently read their horoscope associated to their star sign or find out the readings for others and let them know. I am developing this program for busy people who follow their horoscope, check it constantly and need a way to read it on the fly from their computer, as they spend most of their time on one whether at home, work or school. 

An example of how a user would use this program is a busy professional who likes to start their day off doing small online tasks during breakfast like checking emails, reading the news, etc. They can quickly open the program and receive their daily horoscope that is linked to one specific source. If they liked the reading then it can be saved to a text file and shared to other friends and family members.



### <u>Features</u>

##### <u>Feature 1 - Find out your star sign</u>

This first feature allows the user to find out what star sign they are by telling the program their date of birth and birth month. This is by getting the user to enter them by two inputs. Once submitted, this allows Zodiac Zen to make the correct calculation and return the user's star sign. This is done by running the birth date against a series of date checks within the program. The calculation is done within the program through a if/elif conditional statement.

##### <u>Feature 2 - Retrieve your daily horoscope</u>

This feature allows the user to access their daily horoscope reading which will be displayed to them to read. The user is prompted for their star sign and this then retrieves the reading by using a package called *BeautifulSoup*, which allows a webpage to be scraped of information then saved within the program. This then outputs the daily reading for the user to read. They can also enter other star signs if they wish to access a daily reading for someone else. Each daily reading is stored in a list and then when a star sign is entered, it corresponds with its index (E.g. cancer = horoscope[4]).

##### <u>Feature 3 - Save daily horoscope to a text file</u>

This final feature allows the user to save their daily horoscope reading into a text file and onto their computer. The filename will have the name of the star sign that is being looked up plus the current date. This is so the user will be able to easily collate their readings by sign and date. The user will also be able to store readings of other star signs for other people, say family members, in organised folders if they so desire. 



### <u>User Interaction and Experience</u>

Zodiac Zen was designed with the user in mind. The menu is very clean and straightforward with minimal clicks needed to execute an action. Colour and spacing was strategically used for a better user experience and when the program starts, the user is asked for their name for a personalised greeting making the experience personal.

When the program first opens to the user, they will be shown the day's date and then greeted by the program. They will then be asked for their first name, followed by their last name.

```
				Friday, July 05, 2019

        Welcome! What is your first name? Anne
        And your last name? Homann
```

When submitted, the user will receive a personalised greeting followed by the main menu, which will clearly display the options in a numbered fashion.

```
				Hello Anne Homann! 😇

        🔥 WELCOME TO ZODIAC ZEN!

        PRESS EITHER 1, 2 OR 3 TO MAKE YOUR SELECTION

        (1) What is my star sign?
        (2) Receive my daily horoscope
        (3) Exit
```

If the user selects option 1, the program will first ask them for the day of the month they were born. To prevent an error, the user is advised that only numbers should be typed in.

```
				What day of the month were you born? (numbers only): 25
```

If the user enters a response that is not correct, they will receive the following error:

```
				What day of the month were you born? (numbers only): 324654645635
        Invalid birth date! It must be in the range of 1-31.

        What day of the month were you born? (numbers only): wqtrewhcbsdxg
        Invalid birth date! It must be in the range of 1-31.
```

After the correct birth date has been entered, the next prompt is for their birth month. 

```
				What day of the month were you born? (numbers only): 25

        What month were you born?: 
```

If the user enters a response that is not correct, they will receive the following error:

```
				What month were you born?: fsagsgasa
        Invalid birth month! Please try again.

        What month were you born?: 35465436346
        Invalid birth month! Please try again.
```

When the correct information is submitted, the user will receive their star sign and then they are returned to the main menu.

```
				What day of the month were you born? (numbers only): 25
				
				What month were you born?: june

        Your Astrological sign is: ♋ Cancer
```

If the user decides they want to read their daily horoscope, they would select option 2. Once selected, they are prompted to enter their star sign.

```
				Please enter your star sign: 
```

If the user enters a response that is not correct, they will receive the following error:

```
				Please enter your star sign: 23$%#4356
        Invalid star sign! Please try again.

        Please enter your star sign: sfoiwnesfsdf
        Invalid star sign! Please try again.
```

When a valid star sign is submitted, the user will receive their relevant daily horoscope reading and then asked if they wish to save a copy.

```
				Please enter your star sign: leo

        As Moon is stationed in Aries, some of you maybe presented with several opportunities to get out of a difficult situation. Now is the time to get out of every trouble that has been bothering you. Be wary of a former rival who might try to cause fresh trouble in your life. Your never say die attitude will help you overcome problems that would have scared the rest today. You make new friends but on the downside some challenges on the way may make you feel upset and frustrated. Your lucky color for the day is red and the time between 9 am to 11 am will prove to be lucky for you.

        Would you like to save a copy of your horoscope?
        Y/N?
```

If Y is selected, a copy is saved to their computer as a text file with the star sign and date as the filename. The user will receive feedback that the file has been saved.

```
				Would you like to save a copy of your horoscope?
        Y/N?
        
        File saved!
```

If N is selected, then the user is taken back to the main menu. 

If the user enters a response other than Y or N, they will receive the following error:

```
				Would you like to save a copy of your horoscope?
        Y/N?
        
        safwfa

        PLEASE SELECT EITHER Y/ N
```

The final option is for the user to exit the program. This displays a goodbye message to the user and closes Zodiac Zen.

```
				Thank you for using Zodiac Zen! Goodbye 👋
```



### Control Flow Diagram

![](https://github.com/annehomann/zodiac_zen/blob/master/docs/anne-homann-CSB-flowchart_small.png)

![](https://github.com/annehomann/zodiac_zen/blob/master/docs/anne-homann-CSB-flowchart_legend.png)

- A larger version of the control flow diagram is in the docs folder.



### Implementation Plan

##### <u>Feature 1 - Find our your star sign</u>

This feature will be implemented by writing an if/elif statement that cycles through the star signs until the correct sign is selected that corresponds to the user's birth date and month details. The user will be able to enter their information by using two inputs that captures their answers. After the star sign is displayed, the user is taken back to the main menu.

##### <u>Feature 2 - Retrieve your daily horoscope</u>

This feature will be implemented by first, using BeautifulSoup to scrape the horoscope readings from an HTML page and then store them into a list. As there will be 12 readings within the list, it will be easy to access each one separately by their index number. Again, an if/elif statement will be used to cycle through the star signs. An input will be used to capture the star sign entered by the user and that will determine which horoscope reading is returned.

##### <u>Feature 3 - Save daily horoscope to a text file</u>

This feature is a continuation of feature 2 and will be implemented by using the file.write() method which is included within the if/elif conditional statement. The user is prompted after the reading if they wish to save a copy. If the user enters Y, the reading is written to a text file and saved on their local hard drive. The filename is the star sign that was entered and today's date, (E.g. **capricorn_July 01, 2019.txt**). If the user selects N, then they are returned to the main menu.   

| Feature 1                                                    | Feature 2                                                    | Feature 3                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [  ] Create an input for the user to enter their date of birth (2)<br />[  ] Create an input for the user to enter their month of birth (2)<br />[  ] Use if/elif statement to cycle through star signs (3)<br />[  ] Display correct star sign to user (3)<br />[  ] Take user back to menu (1) | [  ] Create an input for the user to enter their star sign (2)<br />[  ] Use BeautifulSoup for web scraping of horoscopes (3)<br />[  ] Use a list to store scraped readings from each sign (3)<br />[  ] Use indices to access each one (3)<br />[  ] Display daily horoscope reading to user (2)<br /> | [  ] After the reading has been displayed, ask the user if they wish to save their reading (3)<br />[  ] If Y, use a write() method to save the text to a file (3)<br />[  ] Filename will be user's star sign and today's date **(capricorn_July 01, 2019.txt)** (2)<br />[ ] If N, take user back to menu (1) |

Priority key  =   (1) Low     (2) Medium      (3) High

More detailed checklists and deadlines appear on trello board: [Zodiac Zen](https://trello.com/b/5ianrkvy/horoscope-app)

Examples of Trello in use:

![](https://github.com/annehomann/zodiac_zen/blob/master/docs/anne-homann-CSB-project-mgt-trello1.png)

![](https://github.com/annehomann/zodiac_zen/blob/master/docs/anne-homann-CSB-project-mgt-trello2.png)

![](https://github.com/annehomann/zodiac_zen/blob/master/docs/anne-homann-CSB-project-mgt-trello3.png)

![](https://github.com/annehomann/zodiac_zen/blob/master/docs/anne-homann-CSB-project-mgt-trello4.png)

![](https://github.com/annehomann/zodiac_zen/blob/master/docs/anne-homann-CSB-project-mgt-trello5.png)



### <u>**Timeline**</u>

- Create main menu - 28/06/19
- Complete feature 1 - 28/06/19
- Complete feature 2 - 28/06/19
- Complete feature 3 - 29/06//19
- Implement Argparse - 4/07/19
- Unit Testing/Pytest - 5/07/19
- Error Handling - 6/07/19
- Pylint code - 6/07/19
- Package final product - 6/07/19

