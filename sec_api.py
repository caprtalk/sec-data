import requests


class sec_api:

    # api: data.sec.gov/api
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    # get all filings for a given company
    def sec_filings(ticker):



        url = f'https://data.sec.gov/submissions/{CIK}.json}'
        response = requests.get(url)
        if response.status_code == 200:
            pass
        else:
            print('Error: ', response.status_code)

        # store filings in temp directory
        with open(f'./temp/{ticker}.json', 'w') as f:
            f.write(response.text)

