import requests
from selenium import webdriver

def get_filling(ticker):
    url = f'https://www.sec.gov/edgar/search/#/entityName={ticker}'
    response = requests.get(url, stream=True)
    return response

