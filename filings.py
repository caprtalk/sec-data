from sec_edgar_downloader import Downloader
import glob
import shutil
import os


def get_filing(ticker, quant):  # pulls form 4 filings from sec database given ticker and quantity
    path = os.path.dirname(__file__)
    dl = Downloader(f'{path}/temp-sec-filings')
    dl.get('4', ticker, amount=quant)


def clear_filings():  # delete files from directory
    path = os.path.dirname(__file__)
    os.remove(f'{path}/temp-sec-filings/sec-edgar-filings')

def sort_files(ticker):  # moves temp xlm files into correct directory
    path = os.path.dirname(__file__)
    temp_path = glob.glob(f'{path}/temp-sec-filings/sec-edgar-filings/**', recursive=True)
    dst_folder = f'{path}/temp-sec-filings/'
    # Search files with .xml extension in source directory
    file_type = r'\*.xml'
    pos = 3
    count = 1
    while pos < len(temp_path):
        src_folder = temp_path[pos]
        file = glob.glob(src_folder + file_type)
        file = file[0]
        file_name = f'filing-details{count}.xml'
        shutil.move(file, dst_folder + file_name)
        pos += 3
        count += 1


company = input('enter company ticker ')
quantity = input('how many sec-filings ')
get_filing(company, quantity)
sort_files(company)
