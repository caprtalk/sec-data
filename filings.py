from sec_edgar_downloader import Downloader
import os


def get_filing(ticker, quant):
    path = os.path.dirname(__file__)
    dl = Downloader(f'{path}/temp-sec-filings')
    dl.get('4', ticker, amount=quant)


def clear_filings():
    path = os.path.dirname(__file__)
    os.remove(f'{path}/temp-sec-filings/sec-edgar-filings')


company = input('enter company ticker ')
quantity = input('how many sec-filings ')
get_filing(company, quantity)
