import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
import json

def export_data(list_of_stocks):
    export_file = open("stocks.csv", "w")

    #write a header row in the csv file
    header_row = ""
    for key in list_of_stocks[0]:
        header_row += key+","
    
    export_file.write(f"{header_row}\n")

    #loop through list of stocks
    for stock in list_of_stocks:
        stock_record = ""
        #write stock indicators to the file
        for indicator, value in stock.items():
            stock_record += value+", "
        #write record to file
        export_file.write(f"{stock_record}\n")
    
    export_file.close()

    return

def main():
    file = open("stupoid.html", "w")
    to_write = f"<h1>Very cool thing</h1>{datetime.now()}: <br/><br/><hr/>"

    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    
    symbols_list = ["GOOGL", "IBM", "SBUX", "AMC", "NFLX", "TSLA", "BA", "RBLX"]
    list_of_stock_dictionaries = []
    
    for symbol in symbols_list:
        url = f'https://finance.yahoo.com/quote/{symbol}'

        #request the page
        print(f"Requesting data from symbol {symbol} via {url}")
        response = requests.get(url, headers=headers)

        #parse html and create a beautiful soup object
        soup = BeautifulSoup(response.text, 'html.parser')

        #for table in soup.find_all('table', {"class": "W(100%) M(0) Bdcl(c)"}):
        #    print(table)

        stock_dictionary = {}
        stock_dictionary['symbol'] = symbol

        counter = 1
        for cell in soup.find_all('td'):
            #odd iterations are key. Set key on odd numbered interations
            if counter % 2 != 0:
                key = cell.text
            else:
                stock_dictionary[key] = cell.text
            counter += 1
        to_write += f"{symbol}: {stock_dictionary} "
        to_write += "<hr/>"
        list_of_stock_dictionaries.append(stock_dictionary)

        time.sleep(0)

    file.write(to_write)
    export_data(list_of_stock_dictionaries)

main()
