import requests
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
API_key=""
api="https://www.alphavantage.co/query"
parameters={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":API_key
}
response=requests.get(api,params=parameters)
response.raise_for_status()
data=response.json()['Time Series (Daily)']

print(data)
date_today=datetime.datetime.now().date()

number_day_today=datetime.datetime.now().weekday()
number_day_yesterday=number_day_today-1
number_day_before_yesterday=number_day_yesterday-1
if number_day_today==0:
    yesterday = date_today - datetime.timedelta(days=3) # with the function timedelta we substract a day
    if (number_day_today-1)==0:
        day_before_yesterday = yesterday - datetime.timedelta(days=3)
    else:
        day_before_yesterday = yesterday - datetime.timedelta(days=1)
else:
    yesterday = date_today - datetime.timedelta(days=1)
    if number_day_today-1==0:
        day_before_yesterday = yesterday - datetime.timedelta(days=3)
    else:
        day_before_yesterday = yesterday - datetime.timedelta(days=1)



closing_price_yesterday=float(data[str(yesterday)]['4. close'])
closing_price_day_before_yesterday=float(data[str(day_before_yesterday)]['4. close'])
porcentage_stock=round(((closing_price_yesterday-closing_price_day_before_yesterday)/closing_price_yesterday)*100,2)
if porcentage_stock>5 and porcentage_stock<-5:
    print("Get News")
print(closing_price_yesterday)
print(closing_price_day_before_yesterday)
print(porcentage_stock)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

