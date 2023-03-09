# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from collections import ChainMap
import json


service = Service(executable_path="C:\chromedriver110\chromedriver.exe")
driver = webdriver.Chrome(service=service)
def returnDataArray(data):
    retunData =[]
    for row in data:
        retunData.append(row.text)
    return retunData


def print_hi():
    scrapData = []
    URL = 'https://it.pracuj.pl/?pn='

    # Use a breakpoint in the code line below to debug your script.
    for page in range(1, 279):
        URL = "https://it.pracuj.pl/?pn="

        driver.get(URL + str(page))
        time.sleep(1.5)

        source = bs(driver.page_source, 'html.parser')

        boxCard = source.find_all('div', class_='ContentBoxstyles__Wrapper-sc-11jmnka-0')
        for card in boxCard:
            isHomeOffice = card.find_all(attrs={"data-test":'offer-remote-work'})
            contractTypes = card.find_all(attrs={"data-test":'offer-conctract'})
            locations = card.find_all(attrs={"data-test":'offer-location'})
            incomesData = card.find_all(attrs={"data-test":'offer-salary'})
            specialistLevel = card.find_all(attrs={"data-test":'offer-management-level'})
            techStack = card.find_all("div", class_='Chipsstyles__Wrapper-sc-17yerqz-0')
            jobTitles = card.find_all("h3", class_="JobOfferstyles__TitleHeader-sc-1rq6ue2-4")
            cardData = {
                "title": returnDataArray(jobTitles),
                'localizations': returnDataArray(locations),
                'managementLevel': returnDataArray(specialistLevel),
                'typeOfContract': returnDataArray(contractTypes),
                'income': returnDataArray(incomesData),
                'techStack' : returnDataArray(techStack),
                'isHomeOffice' : returnDataArray(isHomeOffice)
            }
            print(cardData)
            scrapData.append(cardData)
    with open('json_dataPL.json', 'w',encoding='utf8') as outfile:
        json.dump(scrapData,outfile,ensure_ascii=False)
    driver.close()

# Press the green button in the gutter to run the script.
print_hi()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
