import filings


def main():
    company = input('enter company ticker ')
    quantity = input('how many sec-fillings ')
    filings.get_filing(company, quantity)


if __name__ == '__main__':
    main()

