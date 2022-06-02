import os
import xml.etree.ElementTree as ET
import load_filings


def read_filing(file):
    tree = ET.parse(file)
    root = tree.getroot()
    print(root[5])


def main():
    num_files = load_filings.load_filings()
    path = os.path.dirname(__file__)
    count = 1
    while count <= num_files:
        read_filing(f'{path}/temp-sec-filings/filing-{count}.xml')
        count += 1
    load_filings.clear_filings()


if __name__ == '__main__':
    main()
