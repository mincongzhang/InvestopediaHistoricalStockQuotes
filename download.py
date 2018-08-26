import pandas as pd
import os
import datetime
from six.moves import urllib

def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

#input args:
#symbol     - string
#start_date - datetime
#end_date   - datetime
def download_data(symbol, start_date=datetime.datetime(2018,1,1), end_date=datetime.date.today()):
    file_path = "../investopedia_data/"+symbol+".csv"
    
    print("Downloading "+symbol)
    #if is_non_zero_file(file_path):
    #    print(file_path+" exists!")
    #    return
    
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
    dataframe_list = pd.read_html(html_content)
    dataframe = dataframe_list[0]
    dataframe.to_csv(file_path)
    
download_data("AAPL",datetime.datetime(2018,8,1),datetime.date.today())
