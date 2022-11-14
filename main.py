import pandas as pd
import requests
import helper

user_input_1 = input("Enter time series ")
user_input_2 = input("Enter symbol ")
user_input_3 = input("Enter interval ")
user_input_4 = input("Enter API Key ")

##function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=ST9MBW2Q7B5KLADU'
#For the API to work, input time series as TIME_SERIES_INTRADAY, input symbol as "IBM", input "interval" as 5min and input apikey as ST9MBW2Q7B5KLADU

try:
  stock_data = helper.get_function(user_input_1,user_input_2,user_input_3,user_input_4)
  print(stock_data)
except Exception as e:
  print (e)
  








