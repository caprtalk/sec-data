from sec_edgar_downloader import Downloader
import os


def get_filing(ticker, quant):
    path = os.path.dirname(__file__)
    dl = Downloader(f'{path}/temp-sec-fillings')
    dl.get('4', ticker, amount=quant)

