import pandas as pd
import os
import datetime
from six.moves import urllib

#input: symbol - string, start_data - datetime, end_date - datetime
#output: valid quotes data - dataframe
def get_quotes(symbol, start_date, end_date):
    #example
    #https://www.investopedia.com/markets/api/partial/historical/?Symbol=BILI&Type=%20Historical+Prices&Timeframe=Hourly&StartDate=Nov+28%2C+2010&EndDate=Dec+05%2C+2018
    url_prefix = "https://www.investopedia.com/markets/api/partial/historical/?"
    url_symbol = "Symbol="+symbol
    url_type = "&Type=%20Historical+Prices"
    url_timeframe = "&Timeframe=Daily"
    
    #"%b" get month short name
    #"%B" get month full name
    url_date_lambda = lambda date : date.strftime("%b")+"+"+date.strftime("%d")+"%2C+"+date.strftime("%y")
    url_start_date="&StartDate="+url_date_lambda(start_date)
    url_end_date="&EndDate="+url_date_lambda(end_date)
    
    url = url_prefix+url_symbol+url_type+url_timeframe+url_start_date+url_end_date
    
    req = urllib.request.Request(url)
    html_content = urllib.request.urlopen(req)
    #skip first row: "Date   Open   High    Low  Adj. Close   Volume"
    dataframe_list = pd.read_html(html_content,skiprows=1)
    dataframe = dataframe_list[0]
    dataframe = dataframe[::-1]
    
    return dataframe
    
#input: symbol - string, date - datetime
#output: valid quotes data - dataframe
def get_quotes_from_date(symbol, date):
    quotes = None
    while(True):
        quotes = get_quotes(symbol, date, date)
        bad_data = False
        if quotes.empty:
            print("quotes is empty!")
            date = date - datetime.timedelta(1)
            print("Trying to get previous date data:"+date.strftime("%Y%m%d"))
            continue
        
        #dataframe format: "Date   Open   High    Low  Adj. Close   Volume"
        current_date_data = quotes[0].tolist()[0]
        if "unavailable" in current_date_data:
            print("Error date data from date"+date.strftime("%Y%m%d")+":"+str(current_date_data))
            date = date - datetime.timedelta(1)
            print("Trying to get previous date data:"+date.strftime("%Y%m%d"))
            continue
            
        #dataframe format: "Date   Open   High    Low  Adj. Close   Volume"    
        current_open_data = quotes[1].tolist()[0]
        if "Dividend" in str(current_open_data):
            print("Error open data from date"+date.strftime("%Y%m%d")+":"+str(current_open_data))
            date = date - datetime.timedelta(1)
            print("Trying to get previous date data:"+date.strftime("%Y%m%d"))
            continue
            
        break
            
    return quotes
