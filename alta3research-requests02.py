#!/usr/bin/python3
"""
- This program gets financial fundamental data from QuickFS.
- Documentation to query the QuickFS API is available here:
https://public-api.quickfs.net/v1/#section/Python-SDK

- In this program, I will not use the SDK, but I will interact with the QuickFS API via HTTPS requests.
- Your personal API key is required. You must store it in a file called "my_quickfs_key".
Put this file in the path you will specify in the variable "key_path" just below the initial imports.

- First, if desired, you can get the complete list of quotes for a specified
country and exchange. In this way, you will know what is available and the format to specify the stock you want:
for example, the Adobe stock is written ADBE:US

- Then, you can answer questions to specify:
    . the specific stock for which you want financial fundamental values
    . the number of years in the past that you want data for
    . the specific value that you want to get (ex: revenue, net_income, eps_basic, shares_basic, lt_debt, roic, etc)
- The QuickFS documentation describes all the numerous available values.

- A free QuickFS account allows a max quota of 500 per day via the API.
- Getting the full fundamental data for a single stock consumes a quota of 10.
- Consequently, with the free account, you can  request data for at most 50 stocks per day since this program
extracts all data for a specific stock.

- Example of requests that this program makes:
a) List supported companies (no quota consumed):
https://public-api.quickfs.net/v1/companies[/{country}][/{exchange}]?api_key={your_api_key}

example: To get the list of all companies in the NASDAQ exchange in the US:
https://public-api.quickfs.net/v1/companies/US/NASDAQ

b) To pull metadata and all financial statements (annual and quarterly) for all periods
for a single stock in one API call for IBM:

GET https://public-api.quickfs.net/v1/data/all-data/IBM:US?api_key={your_api_key}

- Then the program gets the fundamental data from QuickFS which responds in JSON,
translate the JSON in a python structure and prints what you have selected.

"""
import requests
import json

# SPECIFY HERE THE LOCAL PATH & DIRECTORY WHERE THE KEY (file "my_quickfs_key") IS LOCATED:
key_path = "/home/student/.ssh/"

# SPECIFY HERE THE DESIRED COUNTRY AND EXCHANGE:
# See this page for a list of alternative countries and exchanges: https://public-api.quickfs.net/v1/#tag/Companies
country = 'US'

def harvest_key(key_path):
    # This function gets your personal API key contained in the file
    # "my_quickfs_key" located in the directory specified in "key_path"
    with open(key_path + "my_quickfs_key") as file_object:
        my_key = file_object.read()
        my_key = my_key.strip("\n")
        return my_key

def get_stocks_list(country, exchange, my_api_key, QUICKFSAPI):
    # get the list of stocks for the country and exchange specified
    stocks = requests.get(f"{QUICKFSAPI}companies/{country}/{exchange}?api_key={my_api_key}").json()
    return stocks

def get_full_data(stock, my_api_key, QUICKFSAPI):
    # Get the full fundamental data for the specified stock in a python dictionary
    data = requests.get(f"{QUICKFSAPI}data/all-data/{stock}?api_key={my_api_key}").json()
    return(data)

def main():
    """
    This program lists all the stocks in a specific exchange and allows the user to choose one
    of them. The program them gets the data from Quick FS and prints all the fundamental financial
    data obtained for the choosen stock.
    """
    # This is the base URL to which we can add parameters
    QUICKFSAPI = "https://public-api.quickfs.net/v1/"
    # Load the key from the local file
    my_api_key = harvest_key(key_path)

    # Ask user if they want to get the full list of stocks
    want_full_list = input("Do you want the full list of available stocks (y/n)? ")

    if want_full_list.lower() == 'y':
        exchange = input("For which US exchange do you want the list of stocks available (NYSE, NASDAQ, OTC, NYSEARCA, BATS, NYSEAMERICAN) ? ").upper()
        # Get the full list of stocks available for the exchange specified in the country specified
        stocks_list = get_stocks_list(country, exchange, my_api_key, QUICKFSAPI)['data']
        stocks_list.sort()
        print(f"\nThere are {len(stocks_list)} stocks available from QuickFS for the {exchange} in {country}.")
        print(f"Here is the complete list: \n {stocks_list}")

    # User can specify here the specific stock for which to get financial fundamental data
    stock = input("\nPlease indicate for which stock you would like to get fundamental data (ex: ADBE:US): ")

    # Get all the fundamental data for the specified stock
    stock_data = get_full_data(stock, my_api_key, QUICKFSAPI)

    # Ask user how many years of data are desired
    years = int(input("\nHow many years of data do you want to get (1 - 15) ? "))

    # Ask user what data he wants to get
    param_to_extract = input("What parameter do you want to get (ex: revenue, net_income, eps_basic, shares_basic, lt_debt, roic, etc) ? ").lower()
    years_list = []
    value_list = []
    # print headers
    print(f"\nPeriod End Date\t\t{param_to_extract}")
    # fill the lists with data and print the data
    for i in range(0, years):
        year_explicit = stock_data['data']['financials']['annual']['period_end_date'][-1-i]
        years_list.append(year_explicit)

        value_explicit = stock_data['data']['financials']['annual'][param_to_extract][-1-i]
        value_list.append(value_explicit)
        print(f"{year_explicit}\t\t\t{value_explicit}")

if __name__ == '__main__':
    main()