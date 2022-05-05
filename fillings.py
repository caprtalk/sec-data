import requests
from selenium import webdriver


def get_filling(ticker, date):
    if date == '5y':
        url = f'https://www.sec.gov/edgar/search/#/entityName={ticker}&filter_forms=4'
    else:
        url = f'https://www.sec.gov/edgar/search/#/dateRange={date}&entityName={ticker}&filter_forms=4'
    response = requests.get(url, stream=True)
    return response


