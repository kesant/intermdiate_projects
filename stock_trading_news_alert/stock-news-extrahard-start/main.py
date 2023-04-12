import requests
import datetime
import os
from twilio.rest import Client
##########################################FUNCIONES###################################
def day_before_set(day,number_day):
    if number_day == 0:
        day_before = day - datetime.timedelta(days=3)
        number_day_before=4
    else:
        day_before=day - datetime.timedelta(days=1)
        number_day_before=number_day-1
    return day_before,number_day_before
def find_prices(data,day,number_day):
    try:
        price=float(data[str(day)]['4. close'])
    except:
        new_day,new_number=day_before_set(day,number_day)
        price=find_prices(data,new_day,new_number)
        return price
    else:
        return price
def get_news():
    api_endpoint_news = "https://newsapi.org/v2/top-headlines"
    api_key_news = os.environ["API_KEY_NEWS"]
    parameters_news = {
        "q": COMPANY_NAME,
        "from": str(date_today),
        "apiKey": api_key_news,

    }
    response_news = requests.get(api_endpoint_news, params=parameters_news)
    response.raise_for_status()
    data_news = response_news.json()
    print(data_news["articles"][:3])
    return data_news["articles"][:3]


def send_message(news):
    account_sid = "YOUR ACCOUNT_SID"
    auth_token = "YOURA AUTH TOKEN"
    client = Client(account_sid, auth_token)
    for new in news :
        message = client.messages.create(
          body=f"{STOCK} : {porcentage_stock}%\n"
               f"Headline :{new['title']}\n"
               f"Brief :{new['description']}",
          from_="+14066415511",
          to="+593987587609"
        )

    print("message sent succesfully")
######################################################################################
STOCK = "TSLA"
COMPANY_NAME = "Tesla"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api_key=os.environ["API_KEY"]
api="https://www.alphavantage.co/query"
parameters={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":api_key
}
response=requests.get(api,params=parameters)
response.raise_for_status()
data=response.json()['Time Series (Daily)']

print(data)
date_today=datetime.datetime.now().date()
print(date_today)
number_day_today=datetime.datetime.now().weekday()



yesterday,number_day_yesterday=day_before_set(date_today,number_day_today)
day_before_yesterday,number_day_before_yesterday=day_before_set(yesterday,number_day_yesterday)

# if number_day_today==0:
#     yesterday = date_today - datetime.timedelta(days=3) # with the function timedelta we substract a day
#     if (number_day_today-1)==0:
#         day_before_yesterday = yesterday - datetime.timedelta(days=3)
#     else:
#         day_before_yesterday = yesterday - datetime.timedelta(days=1)
# else:
#     yesterday = date_today - datetime.timedelta(days=1)
#     if number_day_today-1==0:
#         day_before_yesterday = yesterday - datetime.timedelta(days=3)
#     else:
#         day_before_yesterday = yesterday - datetime.timedelta(days=1)



closing_price_yesterday=find_prices(data,yesterday,number_day_yesterday)
closing_price_day_before_yesterday=find_prices(data,day_before_yesterday,number_day_before_yesterday)
porcentage_stock=round(((closing_price_yesterday-closing_price_day_before_yesterday)/closing_price_yesterday)*100,2)

if porcentage_stock>0 or porcentage_stock<0:
    news=get_news()
    send_message(news)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


# api_endpoint_news = "https://newsapi.org/v2/top-headlines"
# api_key_news = "747548a3853746f5a5779bc2c05708ba"
# parameters_news = {
#     "q": COMPANY_NAME,
#     "from": str(date_today),
#     "apiKey": api_key_news,
#
# }
# response_news = requests.get(api_endpoint_news, params=parameters_news)
# response.raise_for_status()
# data_news = response_news.json()
# print(data_news["articles"][:3])

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = ""
# auth_token = ""
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#   body="Hello from Twilio",
#   from_="+14066415511",
#   to="+593987587609"
# )
#
# print(message.sid)

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

