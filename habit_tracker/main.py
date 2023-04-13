# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from datetime import  datetime

pixela_endpoint="https://pixe.la/v1/users"
USER=""
TOKEN=""
GRAPH=""

user_params={
    "token" : TOKEN,
    "username" : USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"


}


# response=requests.post(url=pixela_endpoint,json=user_params)# we are putting the params as a json
# response.raise_for_status()
# print(response.text)#it gives us the response as a text

graph_endpoint=f"{pixela_endpoint}/{USER}/graphs"

graph_config={
    "id":GRAPH,
    "name":"Cycling graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"

}
headers={
    "X-USER-TOKEN":TOKEN
}


# requests.post(url=graph_endpoint,json=graph_config,headers=headers)

pixel_creation_endpoint=f"{pixela_endpoint}/{USER}/graphs/{GRAPH}"
today=datetime.now().strftime("%Y%m%d")
# print(today.strftime("%Y%m%d"))
pixel_data={
    "date":today,
    "quantity":"5.3"
}

# response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)

update_endpoint= f"{pixela_endpoint}/{USER}/graphs/{GRAPH}/{today}"
new_pixel_data={
    "quantity":"4.5",
}
#requests.put(url=update_endpoint,json=pixel_data,headers=headers)

delete_endpoint=f"{pixela_endpoint}/{USER}/graphs/{GRAPH}/{today}"
response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)