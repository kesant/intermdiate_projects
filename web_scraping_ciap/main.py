import requests
from bs4 import BeautifulSoup


LINK="https://www.toolify.ai/es/"
response=requests.get(LINK)
result=response.text

