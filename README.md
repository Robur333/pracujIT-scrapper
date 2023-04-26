# Project Name: Web Scraping Job Data from Pracuj.pl

## Overview
This Python script is designed to scrape job data from Pracuj.pl, a popular job search website in Poland, using web scraping techniques. It uses various libraries such as Selenium, Beautiful Soup and Requests to extract relevant data from the website.

## Features
The main features of this script are:

- Scrapes job data from all pages on the website
- Extracts job title, location, management level, type of contract, income, technology stack and remote work availability for each job offer
- Stores the extracted data in a JSON file called json_dataPL.json

## Libraries Used
This script uses the following libraries:

- time
- requests
- BeautifulSoup from bs4
- webdriver and chrome.service from selenium
- collections
- json

## Functions
This script contains the following functions:

- returnDataArray(): This function is used to extract text from a list of BeautifulSoup elements and returns a list of strings.
- print_hi(): This is the main function that executes the web scraping process. It extracts job data from all pages on the website and stores the data in a JSON file.

## Usage
To use this script, follow these steps:

1. Install the required libraries: time, requests, BeautifulSoup, webdriver and chrome.service from selenium, collections, and json.
2. Install the ChromeDriver executable and provide its path in the `executable_path` parameter of the `Service()` method.
3. Run the script by pressing the green button in the PyCharm IDE or running it from the command line using the command: `python web_scraper.py`
4. The script will extract job data from all pages on the website and store the data in a JSON file called json_dataPL.json in the same directory as the script.

## Example Data

Here's an example of the data that the script scrapes:

```json
{
  "title": ["Azure Data Engineer"],
  "localizations": ["Warszawa"],
  "managementLevel": ["starszy specjalista (Senior), ekspert"],
  "typeOfContract": [],
  "income": ["21 000-31 500 z\u0142 / mies. (zal. od umowy)"],
  "techStack": ["Microsoft Azure", "PySpark", "Python"],
  "isHomeOffice": ["Praca zdalna"]
},
{
  "title": ["Konsultant ERP enova365"],
  "localizations": ["Toru\u0144"],
  "managementLevel": ["specjalista (Mid / Regular)"],
  "typeOfContract": [],
  "income": ["7 000-9 000 z\u0142 brutto / mies."],
  "techStack": [],
  "isHomeOffice": []
}
```
The data includes information about job titles, locations, management levels, types of contracts, incomes, tech stacks, and whether the job offers remote work.

## Conclusion
This Python script provides an easy way to extract job data from Pracuj.pl using web scraping techniques. The script can be easily modified to extract additional data or to scrape other job search websites. However, it is important to ensure that the website's terms of use permit web scraping and that the data is used ethically and responsibly.
