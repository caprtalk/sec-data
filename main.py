import os
from bs4 import BeautifulSoup
import load_filings


def read_filing(file):  # function to read xml files
    # parse xml file
    infile = open(file)
    contents = infile.read()
    soup = BeautifulSoup(contents, 'xml')
    # pull filing data from root
    transaction = soup.find_all('transactionShares')
    shares = 0
    for title in transaction:
        print(title)
    return shares


def main():
    num_files = load_filings.load_filings()
    path = os.path.dirname(__file__)
    count = 1
    data = []
    while count <= num_files:
        filing_data = read_filing(f'{path}/temp/filing-{count}.xml')
        data.append(filing_data)
        count += 1
    load_filings.clear_filings()
    print(data)


if __name__ == '__main__':
    main()
