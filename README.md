# Budget Chess Tournament Navigator
![GitHub repo size](https://img.shields.io/github/repo-size/g00d-habitz/Chess_tournaments_finder)
![GitHub last commit](https://img.shields.io/github/last-commit/g00d-habitz/Chess_tournaments_finder)
![GitHub issues](https://img.shields.io/github/issues/g00d-habitz/Chess_tournaments_finder)

## 1. About
This is an application that uses Selenium to look up the prices of train tickets to various tournaments scraped from the chessarbiter website. It returns a list sorted by price needed to buy tickets from our starting station.

In 2023, it was my first resume project, but I also used it to find various cheap tournaments I can compete in as a student on a budget.

Selenium is used because the API for Polish PKP is expensive, and the easiest way to scrape the data was by using Koleo's website, which takes a lot of time to load.
## 2. How to run

### Requirements:
- ![Python](https://img.shields.io/badge/Requires-Python-blue)
- ![Google Chrome](https://img.shields.io/badge/Requires-Google%20Chrome-brightgreen)
- ![Selenium](https://img.shields.io/badge/Requires-Selenium-orange)
- ![webdriver_manager](https://img.shields.io/badge/Requires-webdriver__manager-yellowgreen)

You can install Selenium and webdriver_manager with:
```bash
pip install selenium webdriver_manager
```

After running it with Python it will ask you questions for:
1. Your starting station (e.g. Wrocław)
2. The days you can play (a string like this: dd-mm, dd-mm, dd-mm)
3. What type of tournaments you want to play (klasyczne/classical, szybkie/rapid, or blitz. You can choose all three by typing: 'klasyczne,szybkie,blitz')
4. Your train ticket discount in percentage (e.g. if you're a student from Poland you should reply with "51")

With all that collected it will enter a browser, scrape the tournaments in given dates and look up train tickets. If no connections are found, it will set the price for that route as 9999 (and then discount it :) ).

## 3. What's planned (08.08.2024)

In 2024, I'm coming back to playing tournament chess and developing this program with more ideas and experience. From the top of my head, here's a list of things I'd like to implement or change:
* Cleaning up the old code and variable names, so it's more readable
* Ability to look up prices of tickets more than 30 days in advance (last possible date price checked?)
* Better user input and list presentation (graphical interface?)
* Exception handling
* An update to unusual_stations
* Overall refactoring
* Try to add Czech and Slovak tournaments from Šachové správy website and České dráhy trains
* Additional information about the tournaments (e.g., if it's a single-day or multiple-day event)
* Ability to search in one voivodeship or one and the neighbouring voivodeships
* Finding a faster way of scraping prices
* Coming up with more stuff...

And if I'm really bored, I might also try:
* Setting it up as an API on my raspberry Pi
* Ability to buy tickets for tournament's over 30 days from now as soon as the tickets are available (for lower prices)
* Ability to store all tournaments, mark some as possible or rejected, and receive daily notifications on new tournaments
