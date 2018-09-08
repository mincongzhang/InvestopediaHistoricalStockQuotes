# InvestopediaHistoricalStockQuotes

### API example:

https://www.investopedia.com/markets/api/partial/historical/?Symbol=AAPL&Type=%20Historical+Prices&Timeframe=Hourly&StartDate=Nov+28%2C+2017&EndDate=Dec+05%2C+2018

### Code example:
```py
download_data("AAPL",datetime.datetime(2018,8,1),datetime.date.today())
```

```py
#get dataframe
get_quotes("AAPL",datetime.datetime(2018,8,1),datetime.date.today())
```

```py
#get dataframe for specific day
get_quotes_from_date("AAPL",datetime.datetime(2018,8,1))
```
