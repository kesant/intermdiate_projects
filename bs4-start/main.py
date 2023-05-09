from bs4 import BeautifulSoup

with open ("website.html") as file:
	content=file.read()
# "html.parser" this will help beautifulsoup undertands the content
soup=BeautifulSoup(content,"html.parser")#we create the beautifulSoup class
#print(soup.prettify())#prettify will shows all the content indented


all_anchor_tags=soup.find_all(name="p")# search by name
# to get the text in the anchor tags
for tag in all_anchor_tags:
	#print(tag.getText())
	#to get the link from the anchor tags
	print(tag.get("href"))#with this function you just give the attribute you want to get

heading=soup.find(name="h1",id="name")#only get the first item that only matches the query
#print(heading)
"""
when the name of the class is a reserved keyword in order to not clash
wwith the code we change class to class_
"""
heading=soup.find(name="h3",class_="heading")
#print(heading)

#we specify the css selector selector="p a", indicating
#we are looking for an "a" tag inside a p "tag"
company_url=soup.select_one(selector="p a")
print(company_url)
# we can also use the class or the id in the cs selector
company_url=soup.select_one(selector="#name")
print(company_url)
company_url=soup.select(selector=".heading")

