import pandas as pd
import os
from six.moves import urllib

def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def download_data(symbol, start_date):
    file_path = "../investopedia_data/"+symbol+".csv"
    
    print("Downloading "+symbol)
    #if is_non_zero_file(file_path):
    #    print(file_path+" exists!")
    #    return
    
    #example
    #https://www.investopedia.com/markets/api/partial/historical/?Symbol=BILI&Type=%20Historical+Prices&Timeframe=Hourly&StartDate=Nov+28%2C+2010&EndDate=Dec+05%2C+2018
    url_prefix = "https://www.investopedia.com/markets/api/partial/historical/?"
    url_symbol = "Symbol="+symbol
    url_type = "&Type=%20Historical+Prices"
    url_timeframe = "&Timeframe=Daily"
    
    #"%b" get month short name
    #"%B" get month full name
    url_date_lambda = lambda date : date.strftime("%b")+"+"+date.strftime("%d")+"%2C+"+date.strftime("%y")
    url_start_date="&StartDate="+url_date_lambda(date)
    url_end_date="&EndDate="+url_date_lambda(datetime.datetime.now())
    
    url = url_prefix+url_symbol+url_type+url_timeframe+url_start_date+url_end_date
    
    req = urllib.request.Request(url)
    html_content = urllib.request.urlopen(req)
    dataframe_list = pd.read_html(html_content)
    dataframe = dataframe_list[0]
    dataframe.to_csv(file_path)
