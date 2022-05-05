import fillings


def main():
    company = input('enter company ticker ')
    date = input('past 30 1y 5y 10y ')
    r = fillings.get_filling(company, date)
    print(r)


if __name__ == '__main__':
    main()

