#### **Status Updates**

28/06/2019
<u>Status Update 1 - web scraping roadblock</u>

As this is the first time I am using a package called *Beautiful Soup*, it became quite the learning curve trying to figure out how to scrape specific areas of text from various URLs for each star sign. Due to limited time and a long list of other tasks with higher priority for the assignment, I decided to combat this issue by creating my own HTML page with 12 separate horoscope readings so it was easier to identify each paragraph and link it to it's relative star sign. This is not a practical solution as the HTML page is static and would not offer the user a different reading on different days. The static page only serves as a temporary solution to make the feature work and show how the whole program performs. I will be revisiting this issue in the future once I have more experience with web scraping using this tool and make the feature dynamic.



4/07/2019
<u>Status Update 2 - DRY code challenge</u>

Within the program, there is a feature that allows the user to type in a star sign and receive their daily horoscope. Behind the scenes, the function that makes this work is a <u>write to file function</u> which is repeated 12 times to correspond with each star sign. This makes the code very repetitive and I could not think of a way to make it more concise and efficient no matter how many rewrites. This challenge is another task I will be visiting when I'm more comfortable to refactor the code and make the program more code efficient. 



6/07/2019
<u>Status Update 3 - Testing roadblock</u>
After writing two unit tests for functions web_scrape() (the function that scrapes the daily horoscopes from my HTML page) and greeting() (the function that asks the user for their first and last name then displays a personalised greeting) it occured to me late in the day that these tests, although working and passing successfuly, don't actually test my functions. Which I thought they did. When I became curious and renamed the functions or commented out the imports, I noticed that the tests still passed. I also believe that the way my functions have been written aren't suitable for unit testing so this will be priority when I revisit this project for refactoring when my coding ability is stronger.