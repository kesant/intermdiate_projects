import requests
from bs4 import BeautifulSoup
import pandas

#CONSTANTES
CATEGORIES=["ai-chatbots","video-generator","image-generator","text-to-speech","summarizer"]
PRICING=["paid","free"]
LINK="https://www.toolify.ai"

#LISTAS DE LOS DATOS
titles=[]
descriptions=[]
link_tools=[]
link_images=[]
prices=[]
application=[]

#GET THE HTML
def get_info(category,price):
    response=requests.get(f"{LINK}/es/category/{category}?attributes=pricing-{price}")
    resultados=response.text
    return resultados
#GET THE LINK OF THE TOOL
def link_herramienta(enlace):
    response=requests.get(enlace)
    resultado=response.text
    soup=BeautifulSoup(resultado,"html.parser")
    link_tag=soup.find(name="a", class_="flex-1 flex w-full sm:w-36 sm:inline-flex mx-auto bg-blue-1400 justify-center radius-22 py-2 px-4 sm:px-6 hover:bg-blue-1500 focus:bg-blue-1600 to-view-btn")
    link_final=link_tag.get("href")
    return link_final


#MAKE THE SOUP
for categoria in CATEGORIES:
    for precio in PRICING:
        result=get_info(categoria,precio)
        soup=BeautifulSoup(result,"html.parser")
        #GET THE DATA
        #titulos
        title_tags=soup.find_all(name="a",class_="max-w-full inline-block go-tool-detail-name")[:5]
        [titles.append(title.getText().strip("\n")) for title in title_tags]
        #links de las herramientas
        [link_tools.append(link_herramienta(f'{LINK}{tool.get("href")}')) for tool in title_tags]
        #descripcion
        description_tag=soup.find_all(name="a",class_="mt-3 text-base text-gray-1500 break-words tool-desc leading-7 go-tool-detail-description")[:5]
        [descriptions.append(description.getText().strip("\n")) for description in description_tag]
        # link de las imagenes
        images=soup.find_all(name="a",class_="flex-shrink-0 px-8 pt-9 tool-linear go-tool-detail-pic")[:5]
        [ link_images.append(image.select_one("img").get("src")) for image in images]
        #precio
        [prices.append(precio) for i in range(5)]
        #categoria
        [application.append(categoria) for i in range(5)]


data_dict={
    "Nombre":titles,
    "Descripcion":descriptions,
    "Link de la herramienta":link_tools,
    "Link de la imagen":link_images,
    "Pago/Gratis":prices,
    "Categoria":application
}
data=pandas.DataFrame(data_dict)
print(data)
#data.to_csv("info_herramientas.csv")
data.to_excel("herramientas.xlsx",index=False)#create a csv from the data frame given a path
