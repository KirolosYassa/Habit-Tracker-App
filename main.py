import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
# print(os.getenv("TOKEN"))
USER = "kirolosyassa"

pixela_url = "http://pixe.la"
pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token":os.getenv("TOKEN"),
    "username":USER,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
    }

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_url}/v1/users/{USER}/graphs"

pixel_header = {
    "X-USER-TOKEN":os.getenv("TOKEN"),
}


graph_parameters = {"id":"read_graph",
                    "name":"Read Book",
                    "unit":"commit",
                    "type":"int",
                    "color":"ichou",}

response = requests.post(url=graph_endpoint, json=graph_parameters, headers=pixel_header)
print(response.text)

# # Get My graph
# get_graph_url = f"{pixela_url}/v1/users/{USER}/graphs/{graph_parameters['id']}.html"

# response = requests.get(url=get_graph_url)
# print(response.url)

# Post to graph

# post_to_graph_endpoint = f"{pixela_url}/v1/users/{USER}/graphs/{graph_parameters['id']}/"
# print(post_to_graph_endpoint)
date_time = datetime.now()

today = date_time.strftime("%Y%m%d")
# print(today)

pixel_data = {
    "date": today,
    "quantity": "2",
    }

# response_posting_to_graph = requests.post(url=post_to_graph_endpoint, json=pixel_data, headers=pixel_header)
# print(response_posting_to_graph)