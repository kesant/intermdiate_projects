from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")
yc_web_page=response.text
soup=BeautifulSoup(yc_web_page,"html.parser")
articles=soup.find_all(name="span",class_="titleline")#we find all of the anchor tags with the class  titleline
article_links=[]
article_texts=[]
for article_tag in articles:
    text=article_tag.getText()#we get the text that is inside the taag
    article_texts.append(text)
    link=article_tag.select_one(selector="a").get("href")#we get the link of the title
    article_links.append(link)
article_upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)
highest_score=max(article_upvotes)
index_highest=article_upvotes.index(highest_score)
highest_text=article_texts[index_highest]
highest_link=article_links[index_highest]
print(highest_text)
print(highest_link)