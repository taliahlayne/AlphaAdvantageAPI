import requests

def get_function (time_series,symbol,interval,apikey): 
  
  url = 'https://www.alphavantage.co/query'

  if time_series != "TIME_SERIES_INTRADAY":
    raise Exception("Sorry, wrong time series")
  if symbol != "IBM":
    raise Exception("Sorry, wrong symbol")
  if interval != "5min":
    raise Exception("Sorry, wrong interval")
  if apikey != "ST9MBW2Q7B5KLADU":
    raise Exception("Sorry, wrong apikey")

  
  r = requests.get(url + "?"+ "function=" + time_series + "&" + "symbol=" + symbol + "&" "interval=" + interval + "&" + "apikey=" + apikey)
  data = r.json()
  return data

