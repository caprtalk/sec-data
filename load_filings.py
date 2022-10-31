from sec_edgar_downloader import Downloader
import glob
import shutil
import os


def get_filing(ticker, quant):  # pulls form 4 filings from sec database given ticker and quantity
    path = os.path.dirname(__file__)
    dl = Downloader(f'{path}/temp')
    dl.get('4', ticker, amount=quant)


def clear_folder():  # removes unwanted directory after sort
    path = os.path.dirname(__file__)
    clear_path = f'{path}/temp/sec-edgar-filings'
    shutil.rmtree(clear_path)


def sort_files():  # moves temp xml files into correct directory
    path = os.path.dirname(__file__)
    temp_path = glob.glob(f'{path}/temp/sec-edgar-filings/**', recursive=True)
    dst_folder = f'{path}/temp/'
    # Search files with .xml extension in source directory
    file_type = r'/*.xml'
    pos = 3
    count = 1
    while pos < len(temp_path):  # moves each file from edgar database to correct folder
        src_folder = temp_path[pos]
        file = glob.glob(src_folder + file_type)
        file = file[0]
        file_name = f'filing-{count}.xml'
        shutil.move(file, dst_folder + file_name)
        pos += 3
        count += 1
    clear_folder()
    return count - 1


def load_filings():  # loads requested filings from edgard database into the temp folder
    company = input('ticker: ')
    quantity = input('number of filings ')
    get_filing(company, quantity)
    num_filings = sort_files()
    return num_filings


def clear_filings():  # clears all sec filings from temp folder after they have been read
    path = os.path.dirname(__file__)
    src_folder = f'{path}/temp'
    # Search files with .xml extension in source directory
    file_type = r'/*.xml'
    files = glob.glob(src_folder + file_type)
    for file in files:
        os.remove(file)

load_filings()