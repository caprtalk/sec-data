import os
from bs4 import BeautifulSoup
import load_filings


def read_filing(file):  # function to read xml files
    # parse xml file
    infile = open(file)
    contents = infile.read()
    soup = BeautifulSoup(contents, 'xml')
    # pull filing data from root
    titles = soup.find_all('transactionShares')
    thing = 0
    for title in titles:
        title = int(title)
        thing += title
    return thing


def main():
    num_files = load_filings.load_filings()
    path = os.path.dirname(__file__)
    count = 1
    data = []
    while count <= num_files:
        filing_data = read_filing(f'{path}/temp-sec-filings/filing-{count}.xml')
        data.append(filing_data)
        count += 1
    load_filings.clear_filings()
    print(data)


if __name__ == '__main__':
    main()
